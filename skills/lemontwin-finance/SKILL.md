---
name: lemontwin-finance
version: 1.0.0
description: "LemonTwin 財務摘要：營收、應收、人工、淨額。use for 對帳, 應收, finance, 出貨."
tags: [lemontwin, finance]
user-invocable: true
metadata: {"openclaw":{"emoji":"💰","requires":{"bins":["curl","jq"]}}}
---

# 果園財務摘要

1. `lemontwin-api` → `finance`
2. 產出：出貨營收、應收未結、人工成本、淨額估算
3. 若有 `pendingPaymentCount`，列待收款批數與建議跟進（不自動改帳）

可與 **lemontwin-daily-briefing** 合併週報。
