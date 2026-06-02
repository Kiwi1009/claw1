---
name: lemontwin-daily-briefing
version: 1.0.0
description: "產出 LemonTwin 果園每日晨報：KPI、警示、值班、待辦優先序。use for 晨報, 今日果園, daily briefing, LemonTwin."
tags: [lemontwin, briefing, orchard]
user-invocable: true
metadata: {"openclaw":{"emoji":"📋","requires":{"bins":["curl","jq"]}}}
---

# 果園每日晨報

## 流程

1. 讀取 skill **lemontwin-api**，執行：
   - `operations`
   - `weather-today`
   - `tasks`
2. 可選：`finance`、`cameras`（若有離線鏡頭列入警示）
3. 產出 **繁體中文** 晨報，結構：

- **今日值班**
- **天氣與農務建議**（1 段）
- **三項優先**（緊急任務、逾期、採後/庫存/應收擇要）
- **KPI 一行**（產量、在庫、開放任務、高風險樹）
- **待確認**（缺資料時列項）

4. 寫入 `workspace/automation/outputs/lemontwin-briefing-YYYY-MM-DD.md`（Asia/Taipei 日期）

## 邊界

- 不自動對外發訊息，除非使用者明確要求
- 不自動大量開任務；若要派工請用 **lemontwin-weather-duty**
