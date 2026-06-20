# OpenClaw 製造業功能網頁

## 整合架構（與 Gateway 同一埠）

| 路徑 | 內容 |
|------|------|
| `/` | 製造業功能首頁（**25** 項工具，可搜尋／分類） |
| `/pages/*` | 各功能表單頁 |
| `/openclaw/` | **OpenClaw Control UI**（與 Agent 對話） |

對外網域（例如 `https://claw1.graceai.net/`）在 Gateway 重啟並啟用 `manufacturing-portal` 插件後，根路徑即為製造首頁；控制台在 `/openclaw/`。

## 自動化排程（Cron）

首頁「自動化排程」區說明三項背景任務（非網頁表單）：

| 排程 | 輸入 | 輸出 |
|------|------|------|
| 每天 07:30 班次交接 | `automation/inputs/shift-handoff-input.md` | `automation/outputs/shift-handoff-*.md` |
| 每週一 09:00 倉儲週報 | `automation/inputs/inventory.csv` | `automation/outputs/warehouse-weekly-*.md` |
| 每天 08:00 設備保養 | `automation/inputs/equipment.csv` | `automation/outputs/maintenance-daily-*.md` |

安裝：`./scripts/setup-manufacturing-cron.sh`（詳見 `automation/README.md`）。

## 視覺主題

全站（首頁 + 25 個工具頁）採用同一套**淺色工業風**：

- `assets/css/style.css` — 全站共用
- `assets/css/home.css` — 首頁專用區塊

## 樣式載入（Gateway）

製造入口透過 `manufacturing-portal` 插件提供靜態檔。OpenClaw 的 `/` 前綴路由**不會**涵蓋 `/assets`、`/pages`，插件已額外註冊這兩條路徑。若首頁無樣式，請確認：

```bash
curl -I http://127.0.0.1:28789/assets/css/style.css   # 應為 200
openclaw gateway restart
```

對外網域若仍無樣式，可能是 Cloudflare 快取了舊的 404；強制重新整理或等快取過期（約 4 小時）。

## 本機開發（僅靜態預覽）

```bash
cd web && python3 -m http.server 8080
```

此模式 **不會** 提供 `/openclaw/`，僅供預覽表單 UI。完整整合請使用 Gateway：

```bash
openclaw gateway restart
```

然後開啟 Gateway 埠（預設 **28789**）：

- http://127.0.0.1:28789/ — 製造首頁
- http://127.0.0.1:28789/openclaw/ — OpenClaw 控制台

## 設定位置

- 插件：`workspace/.openclaw/extensions/manufacturing-portal/`
- Gateway：`~/.openclaw/openclaw.json` → `gateway.controlUi.basePath: "/openclaw"`
- 插件開關：`plugins.entries.manufacturing-portal.enabled: true`

## 25 項工具

首頁由 `assets/js/tools-data.js` 驅動，含搜尋與分類篩選。新增頁面可執行 `python3 scripts/generate-pages.py` 或手動加入 `tools-data.js`。

完整列表見首頁；主要對應 skills 含：mes、manufacturing-shift-handoff、quotation-workflow、rohoon-6sigma、complaint-8d-report、integrated-manufacturing-consulting 等。
