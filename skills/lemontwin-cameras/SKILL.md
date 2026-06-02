---
name: lemontwin-cameras
version: 1.0.0
description: "LemonTwin 四路監控：狀態、截圖、AI 初篩。use for 攝影機, RTSP, 監控, snapshot."
tags: [lemontwin, camera, hikvision]
user-invocable: true
metadata: {"openclaw":{"emoji":"📹","requires":{"bins":["curl","jq"]}}}
---

# 果園監控

1. `lemontwin-api` → `cameras` — 四路狀態、最新截圖 URL
2. 若使用者要求立即截圖：`snapshot-all`（需 RTSP 與 ffmpeg 已設定）
3. 彙整 `reviewRequired` 的截圖，建議派給**值班**複查
4. 安裝教學（給人類）：`/Users/joycechen/LemonTwin/docs/camera-installation.md`  
   網站：`https://orchard.graceai.net/cameras/install`

即時 HLS 僅經 tunnel `/streams`，勿在對話中貼 RTSP 帳密。
