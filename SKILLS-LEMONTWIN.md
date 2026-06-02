# LemonTwin / 果園 OpenClaw Skills 目錄

## 已安裝（本機 workspace）

### ClawHub（農業通用）

| Skill | 用途 |
|-------|------|
| `farm-task-manager` | 農場待辦、週期任務、優先序 |
| `agriculture` | 作物、庫存、設備、天氣、財務綜合管理框架 |
| `ai-intelligent-agriculture-monitoring` | 作物監測、病蟲害識別（通用） |

安裝更多：`openclaw skills search <關鍵字>` → `openclaw skills install <名稱>`

### LemonTwin 專用（接 API）

| Skill | 用途 |
|-------|------|
| `lemontwin-api` | 核心 API 腳本（operations / 天氣 / 任務…） |
| `lemontwin-daily-briefing` | 每日晨報 → `automation/outputs/` |
| `lemontwin-weather-duty` | 天氣評估 + 值班派工 |
| `lemontwin-harvest` | 採收登記與採後任務 |
| `lemontwin-cameras` | 四路監控與截圖 |
| `lemontwin-finance` | 財務摘要 |
| `orchard-shift-handoff` | 果園班次交接 |

## 快速測試

```bash
export LEMONTWIN_API_BASE="http://127.0.0.1:3001/api"
~/.openclaw/workspace/skills/lemontwin-api/scripts/lemontwin.sh login
~/.openclaw/workspace/skills/lemontwin-api/scripts/lemontwin.sh operations
```

需先啟動 LemonTwin API：`cd /Users/joycechen/LemonTwin/api && npm run dev`

## 建議再安裝（ClawHub 搜尋結果）

```bash
openclaw skills install orchard-fruit-trees    # 果樹栽培知識
openclaw skills search monitoring              # 其他監測類
```

## 與製造業 skills 分工

- **製造**（mes、8d、spc…）→ 工廠產線  
- **lemontwin-*** → 檸檬果園真實資料（同一台 OpenClaw，不同 skill 名稱觸發）

## Cron 範例

見 `cron/jobs.json` 製造業範例；可新增：

- 每日 07:00 → 讀 `lemontwin-daily-briefing`
- 每日 06:30 → 讀 `lemontwin-weather-duty`
- 每日 17:00 → 讀 `orchard-shift-handoff`
