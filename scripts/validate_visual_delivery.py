#!/usr/bin/env python3
"""Validate the non-negotiable provenance and review contract for visual delivery."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

INTERNAL_MARKERS = ("layout only", "private sample", "fixture", "placeholder", "검수용")
REQUIRED_ART_DIRECTION = ("scene", "camera", "copy_hierarchy", "palette", "must_keep", "must_avoid")
REQUIRED_RED_CHECKS = ("reference_fidelity", "scene_and_composition", "copy_and_color", "user_facing_completeness")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def resolve(manifest_path: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else manifest_path.parent / path


def existing_file(data: dict, manifest_path: Path, key: str, errors: list[str]) -> Path | None:
    value = data.get(key)
    if not isinstance(value, str) or not value:
        fail(errors, f"{key} path is required")
        return None
    path = resolve(manifest_path, value)
    if not path.is_file():
        fail(errors, f"{key} does not exist: {value}")
        return None
    return path


def image_file(data: dict, manifest_path: Path, key: str, errors: list[str]) -> Path | None:
    path = existing_file(data, manifest_path, key, errors)
    if path is None:
        return None
    try:
        with Image.open(path) as image:
            image.verify()
    except (OSError, ValueError) as exc:
        fail(errors, f"{key} is not a decodable image: {exc}")
    return path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(data: dict, require_user_preview: bool, manifest_path: Path) -> list[str]:
    errors: list[str] = []
    delivery_class = data.get("delivery_class")
    if delivery_class not in {"user_preview", "internal_scaffold"}:
        fail(errors, "delivery_class must be user_preview or internal_scaffold")
        return errors
    if require_user_preview and delivery_class != "user_preview":
        fail(errors, "a user-facing delivery cannot be an internal_scaffold")
    if delivery_class == "internal_scaffold":
        return errors

    if data.get("renderer_mode") not in {"image_generation", "image_editing"}:
        if not data.get("code_native_final_approved"):
            fail(errors, "user_preview requires image_generation or image_editing")
    refs = data.get("reference_inputs")
    if not isinstance(refs, list) or not refs:
        fail(errors, "user_preview requires at least one actual reference_input")
    else:
        for index, ref in enumerate(refs):
            if not isinstance(ref, dict) or not ref.get("path") or not ref.get("role"):
                fail(errors, f"reference_inputs[{index}] needs path and role")
            else:
                ref_path = resolve(manifest_path, ref["path"])
                try:
                    with Image.open(ref_path) as image:
                        image.verify()
                except (OSError, ValueError) as exc:
                    fail(errors, f"reference_inputs[{index}] is not a decodable image: {exc}")
                    continue
                if ref.get("sha256") != sha256(ref_path):
                    fail(errors, f"reference_inputs[{index}] must include the image SHA-256")
    direction = data.get("art_direction")
    if not isinstance(direction, dict):
        fail(errors, "art_direction object is required")
    else:
        for field in REQUIRED_ART_DIRECTION:
            if not direction.get(field):
                fail(errors, f"art_direction.{field} is required")
    if not isinstance(data.get("rendered_copy"), list):
        fail(errors, "rendered_copy list is required for internal-copy leakage checks")
    else:
        copy = " ".join(str(item).lower() for item in data["rendered_copy"])
        for marker in INTERNAL_MARKERS:
            if marker in copy:
                fail(errors, f"user_preview leaks internal marker: {marker}")
    if not isinstance(data.get("iteration_count"), int) or data["iteration_count"] < 1:
        fail(errors, "iteration_count must record at least the first rendered pass")
    candidates = data.get("candidate_assets")
    if not isinstance(candidates, list) or len(candidates) < data.get("iteration_count", 0):
        fail(errors, "candidate_assets must retain a real file for every rendered iteration")
    else:
        for index, item in enumerate(candidates):
            if not isinstance(item, str):
                fail(errors, f"candidate_assets[{index}] must be a path")
                continue
            try:
                with Image.open(resolve(manifest_path, item)) as image:
                    image.verify()
            except (OSError, ValueError) as exc:
                fail(errors, f"candidate_assets[{index}] is not a decodable image: {exc}")
    final_asset = image_file(data, manifest_path, "final_asset", errors)
    comparison_path = image_file(data, manifest_path, "reference_candidate_comparison", errors)
    red_path = existing_file(data, manifest_path, "red_report", errors)
    if red_path is not None:
        report = red_path.read_text(encoding="utf-8", errors="replace").lower()
        for required in ("pass", "reference", "scene", "copy", "internal"):
            if required not in report:
                fail(errors, f"red_report must contain a concrete {required} finding")
    ocr_path = existing_file(data, manifest_path, "ocr_evidence", errors)
    if ocr_path is not None and final_asset is not None:
        try:
            ocr_data = json.loads(ocr_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            fail(errors, "ocr_evidence must be JSON from an actual rendered-asset inspection")
            ocr_data = {}
        if not ocr_data.get("engine") or ocr_data.get("source_sha256") != sha256(final_asset):
            fail(errors, "ocr_evidence must name an engine and bind to final_asset SHA-256")
        ocr = str(ocr_data.get("text", "")).lower()
        for marker in INTERNAL_MARKERS:
            if marker in ocr:
                fail(errors, f"OCR evidence finds internal marker in final asset: {marker}")
    request_path = existing_file(data, manifest_path, "generation_request_evidence", errors)
    if request_path is not None and isinstance(refs, list):
        try:
            request_data = json.loads(request_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            fail(errors, "generation_request_evidence must be machine-readable JSON")
            request_data = {}
        if request_data.get("operation") not in {"image_generation", "image_editing"} or not request_data.get("request_id"):
            fail(errors, "generation_request_evidence needs image operation and request_id")
        request_refs = request_data.get("referenced_image_paths", [])
        for ref in refs:
            if isinstance(ref, dict) and isinstance(ref.get("path"), str) and ref["path"] not in request_refs:
                fail(errors, f"generation request evidence does not include reference: {ref['path']}")
    response_path = existing_file(data, manifest_path, "generation_response_evidence", errors)
    if response_path is not None and request_path is not None and final_asset is not None:
        try:
            response_data = json.loads(response_path.read_text(encoding="utf-8"))
            request_data = json.loads(request_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            fail(errors, "generation_response_evidence must be machine-readable JSON")
            response_data, request_data = {}, {}
        if response_data.get("request_id") != request_data.get("request_id"):
            fail(errors, "generation response must match the recorded generation request")
        if response_data.get("output_asset") != data.get("final_asset") or response_data.get("output_sha256") != sha256(final_asset):
            fail(errors, "generation response must bind to final_asset and its SHA-256")
    review = data.get("visual_review")
    if not isinstance(review, dict) or review.get("comparison") != "side_by_side_reference_candidate" or comparison_path is None:
        fail(errors, "visual_review.comparison must be side_by_side_reference_candidate")
    red = data.get("red_visual_review")
    if not isinstance(red, dict):
        fail(errors, "red_visual_review is required")
    else:
        for check in REQUIRED_RED_CHECKS:
            if red.get(check) != "pass":
                fail(errors, f"red_visual_review.{check} must be pass")
    red_evidence_path = existing_file(data, manifest_path, "red_visual_review_evidence", errors)
    if red_evidence_path is not None:
        try:
            red_evidence = json.loads(red_evidence_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            fail(errors, "red_visual_review_evidence must be JSON")
            red_evidence = {}
        for check in REQUIRED_RED_CHECKS:
            finding = red_evidence.get(check, {})
            if finding.get("status") != "pass" or not finding.get("evidence"):
                fail(errors, f"red_visual_review_evidence.{check} needs pass and concrete evidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--require-user-preview", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read manifest: {exc}")
        return 2
    errors = validate(data, args.require_user_preview, args.manifest)
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: visual delivery contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
