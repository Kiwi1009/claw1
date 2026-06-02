---
name: orchard-shift-handoff
version: 1.0.0
description: "檸檬果園班次交接：採收、冷庫、任務、天氣、監控。use for 果園交接, orchard handoff, 值班交接."
tags: [orchard, lemontwin, handoff]
user-invocable: true
metadata: {"openclaw":{"emoji":"🍋","requires":{"bins":["curl","jq"]}}}
---

# 果園班次交接

參考製造業 `manufacturing-shift-handoff` 結構，資料來自 LemonTwin API。

## 流程

1. `lemontwin-api`：`operations`、`tasks`、`weather-today`、`harvests`（最近）
2. 產出結構：
   - 班次摘要
   - 分區樹勢 / 高風險棵數
   - 今日採收與冷庫
   - 開放任務（緊急/逾期標示）
   - 天氣與值班
   - 監控異常（若有）
   - 下班次重點
   - 待確認項

3. 輸出：`workspace/automation/outputs/orchard-handoff-YYYY-MM-DD.md`

## 輸入檔（可選）

`workspace/automation/inputs/orchard-handoff-input.md` — 現場口頭補充
