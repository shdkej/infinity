#!/usr/bin/env bash
set -euo pipefail

asset_root="/home/ubuntu/.openclaw/workspace/media/inbound/openclaw-staged-7ea2b541-0ce0-46ef-9f7f-d3981541bee6"
output="artifacts/content-amalfi-ravello-day-reel-20260918/final/amalfi-ravello-day-reel.mp4"
font="Noto Sans CJK KR"

ffmpeg -y \
  -loop 1 -t 4 -i "$asset_root/input-19dd485a-1cbb-4b41-8b98-e8bb58065c37.jpg" \
  -loop 1 -t 4 -i "$asset_root/input-2f7eeed5-5636-4736-8390-ba1d2f30a63c.jpg" \
  -loop 1 -t 4 -i "$asset_root/input-14f63c50-5cbe-45cf-a6ae-caef515b1e15.jpg" \
  -loop 1 -t 5 -i "$asset_root/input-5d556cb2-cd71-44ec-acef-24b92d6d246d.jpg" \
  -loop 1 -t 6 -i "$asset_root/input-74ddb43f-b88e-463c-b9de-0c7e29397091.jpg" \
  -loop 1 -t 5 -i "$asset_root/input-3ab64e38-3b08-4508-9062-49177d9544e8.jpg" \
  -filter_complex "
    [0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.16:t=fill,drawtext=font='${font}':text='AMALFI / RAVELLO':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=1560:shadowcolor=black@0.7:shadowx=2:shadowy=3[v0];
    [1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.16:t=fill,drawtext=font='${font}':text='INTO THE DAY':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=1600:shadowcolor=black@0.7:shadowx=2:shadowy=3[v1];
    [2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.12:t=fill,drawtext=font='${font}':text='AMALFI, MIDDAY':fontcolor=white:fontsize=52:x=(w-text_w)/2:y=1600:shadowcolor=black@0.7:shadowx=2:shadowy=3[v2];
    [3:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.14:t=fill,drawtext=font='${font}':text='UP TO RAVELLO':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=1600:shadowcolor=black@0.7:shadowx=2:shadowy=3[v3];
    [4:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.1:t=fill,drawtext=font='${font}':text='DOORS WITHIN DOORS':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=1530:shadowcolor=black@0.7:shadowx=2:shadowy=3[v4];
    [5:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,drawbox=x=0:y=0:w=1080:h=1920:color=black@0.2:t=fill,drawtext=font='${font}':text='NIGHT FALLS':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=1600:shadowcolor=black@0.7:shadowx=2:shadowy=3[v5];
    [v0][v1][v2][v3][v4][v5]concat=n=6:v=1:a=0,format=yuv420p[v]
  " -map '[v]' -r 30 -movflags +faststart -c:v libx264 -crf 19 -preset medium "$output"
