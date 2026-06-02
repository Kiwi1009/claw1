---
name: lemontwin-api
version: 1.0.0
description: "呼叫 LemonTwin 果園 API（經營總覽、任務、天氣、採收、監控、財務）。use for LemonTwin, 檸檬果園, demo-farm, orchard API."
tags: [lemontwin, orchard, agriculture, api]
user-invocable: true
metadata: {"openclaw":{"emoji":"🍋","requires":{"bins":["curl","jq"]}}}
---

# LemonTwin API

連線本機或 tunnel 上的 LemonTwin NestJS API（預設 `http://127.0.0.1:3001/api`）。

## 環境變數（見 workspace `TOOLS.md`）

- `LEMONTWIN_API_BASE` — 例：`http://127.0.0.1:3001/api` 或 `https://orchard.graceai.net/api`
- `LEMONTWIN_FARM_ID` — 預設 `demo-farm`
- `LEMONTWIN_EMAIL` / `LEMONTWIN_PASSWORD` — Demo：`inspector@lemontwin.test` / `demo1234`

## 指令

腳本路徑：`{baseDir}/scripts/lemontwin.sh`

```bash
# 登入並快取 JWT
"{baseDir}/scripts/lemontwin.sh" login

# 經營總覽 KPI
"{baseDir}/scripts/lemontwin.sh" operations

# 天氣與值班
"{baseDir}/scripts/lemontwin.sh" weather-today
"{baseDir}/scripts/lemontwin.sh" weather-evaluate

# 任務、月度派工
"{baseDir}/scripts/lemontwin.sh" tasks
"{baseDir}/scripts/lemontwin.sh" dispatch 5 2026

# 採收、財務、監控、樹勢
"{baseDir}/scripts/lemontwin.sh" harvests
"{baseDir}/scripts/lemontwin.sh" finance
"{baseDir}/scripts/lemontwin.sh" cameras
"{baseDir}/scripts/lemontwin.sh" snapshot-all
"{baseDir}/scripts/lemontwin.sh" trees
```

## 派工規則（與系統一致）

- **緊急樹勢任務** → 陳大明
- **天氣 / 監控 AI 複查** → 當日**值班**（API 天氣 evaluate 會處理）

## 專案路徑

LemonTwin 原始碼：`/Users/joycechen/LemonTwin`
