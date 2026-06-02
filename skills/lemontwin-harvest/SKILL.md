---
name: lemontwin-harvest
version: 1.0.0
description: "LemonTwin 採收登記、庫存與採後任務。use for 採收, harvest, 入庫, 採後."
tags: [lemontwin, harvest, post-harvest]
user-invocable: true
metadata: {"openclaw":{"emoji":"🧺","requires":{"bins":["curl","jq"]}}}
---

# 採收與採後

## 查詢

```bash
"{baseDir}/../lemontwin-api/scripts/lemontwin.sh" harvests
```

## 登記（需 curl + token）

使用者提供：分區（A/B/C/D）、重量 kg、等級（A/B/C）時，呼叫 API：

```bash
TOKEN=$(cat ~/.openclaw/workspace/.lemontwin-token)
curl -sf -X POST "$LEMONTWIN_API_BASE/farms/$LEMONTWIN_FARM_ID/harvests" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"zoneCode":"A","weightKg":120,"grade":"A","createInventory":true,"spawnPostHarvestTasks":true}'
```

## 輸出

- 批號、入庫狀態、自動產生的採後任務 ID 列表
- 提醒：採後肥、清園、分級等見任務看板
