---
name: lemontwin-weather-duty
version: 1.0.0
description: "依中央氣象與規則評估天氣，派工給當日值班。use for 天氣派工, CWA, 值班, weather evaluate."
tags: [lemontwin, weather, duty]
user-invocable: true
metadata: {"openclaw":{"emoji":"🌧️","requires":{"bins":["curl","jq"]}}}
---

# 天氣評估與值班派工

1. 確認 LemonTwin API 與 `CWA_API_KEY`（無 key 時為示範資料，晨報需註明）
2. 執行 `lemontwin-api` → `weather-evaluate`
3. 再執行 `tasks`，篩選今日新建、assignee 為值班、taskType 含 `WEATHER_`
4. 用白話總結：今日風險、已開幾張任務、值班人姓名

**禁止**將天氣任務改派給陳大明（除非使用者明確覆寫）。
