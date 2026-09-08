#!/usr/bin/env python3
"""Regression tests for the visual delivery contract."""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

from PIL import Image

SCRIPT = Path(__file__).with_name("validate_visual_delivery.py")
spec = importlib.util.spec_from_file_location("visual_delivery", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)

root = Path(tempfile.mkdtemp())
for name in ("ref.jpg", "candidate-01.png", "candidate-02.png", "final.png", "comparison.png"):
    Image.new("RGB", (16, 16), "white").save(root / name)
(root / "red.md").write_text("PASS: reference scene copy internal checked", encoding="utf-8")
(root / "request.json").write_text(json.dumps({"operation": "image_editing", "request_id": "req-1", "referenced_image_paths": ["ref.jpg"]}), encoding="utf-8")

VALID = {
    "delivery_class": "user_preview",
    "renderer_mode": "image_editing",
    "reference_inputs": [{"path": "ref.jpg", "role": "style_and_typography_reference", "sha256": module.sha256(root / "ref.jpg")}],
    "art_direction": {"scene": "train seat", "camera": "top-down", "copy_hierarchy": "hook then memo", "palette": "neon lime only", "must_keep": ["marker hook"], "must_avoid": ["round table"]},
    "rendered_copy": ["오늘은 여기까지 해도 된다"],
    "iteration_count": 2,
    "candidate_assets": ["candidate-01.png", "candidate-02.png"],
    "final_asset": "final.png",
    "reference_candidate_comparison": "comparison.png",
    "red_report": "red.md",
    "ocr_evidence": "ocr.txt",
    "generation_request_evidence": "request.json",
    "generation_response_evidence": "response.json",
    "red_visual_review_evidence": "red-evidence.json",
    "visual_review": {"comparison": "side_by_side_reference_candidate"},
    "red_visual_review": {"reference_fidelity": "pass", "scene_and_composition": "pass", "copy_and_color": "pass", "user_facing_completeness": "pass"},
}

manifest = root / "render-manifest.json"
manifest.write_text(json.dumps(VALID), encoding="utf-8")
(root / "ocr.txt").write_text(json.dumps({"engine": "manual-red-render-inspection", "source_sha256": module.sha256(root / "final.png"), "text": "오늘은 여기까지"}), encoding="utf-8")
(root / "response.json").write_text(json.dumps({"request_id": "req-1", "output_asset": "final.png", "output_sha256": module.sha256(root / "final.png")}), encoding="utf-8")
(root / "red-evidence.json").write_text(json.dumps({key: {"status": "pass", "evidence": "rendered file inspected"} for key in module.REQUIRED_RED_CHECKS}), encoding="utf-8")
assert module.validate(VALID, True, manifest) == []
leaked = {**VALID, "rendered_copy": ["LAYOUT ONLY · PRIVATE SAMPLE"]}
assert any("leaks internal marker" in error for error in module.validate(leaked, True, manifest))
scaffold = {"delivery_class": "internal_scaffold"}
assert any("cannot be an internal_scaffold" in error for error in module.validate(scaffold, True, manifest))
missing_ref = {**VALID, "reference_inputs": [{"path": "missing.jpg", "role": "style"}]}
assert any("not a decodable image" in error for error in module.validate(missing_ref, True, manifest))
print("PASS: visual delivery contract regression tests")
