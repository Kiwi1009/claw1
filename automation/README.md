# 製造業自動排程

三項預設 Cron 任務，由 OpenClaw Gateway 定時觸發 **Agent + Skill**（非網頁表單）。

## 排程一覽

| 名稱 | 時間（台北） | Skill | 輸入 | 輸出 |
|------|-------------|-------|------|------|
| 製造-每日班次交接 | 每天 07:30 | manufacturing-shift-handoff | `inputs/shift-handoff-input.md` | `outputs/shift-handoff-YYYY-MM-DD.md` |
| 製造-每週倉儲週報 | 每週一 09:00 | warehouse-reports | `inputs/inventory.csv` | `outputs/warehouse-weekly-YYYY-MM-DD.md` |
| 製造-每日設備保養 | 每天 08:00 | equipment-maintenance-log | `inputs/equipment.csv` | `outputs/maintenance-daily-YYYY-MM-DD.md` |

## 安裝排程

```bash
cd /Users/joycechen/.openclaw/workspace
./scripts/setup-manufacturing-cron.sh
```

需 Gateway 已啟動：`openclaw gateway status`

## 管理

```bash
openclaw cron list
openclaw cron run <job-id>          # 立即測試
openclaw cron runs --id <job-id>      # 執行紀錄
openclaw cron disable <job-id>
```

控制台：**/openclaw/** → Cron 區塊

## 啟用推播（選用）

預設 `--no-deliver` 只寫入 `outputs/`。若要送到 LINE／Discord，編輯任務：

```bash
openclaw cron edit <job-id> --announce --channel <你的通道>
```

## 每日維護

- 更新 `inputs/shift-handoff-input.md`（班別交接）
- 更新 `inputs/inventory.csv`（從 WMS 匯出）
- 更新 `inputs/equipment.csv`（設備主檔）
