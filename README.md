# claw1

`claw1` 是一個以 OpenClaw 為核心的製造業工作台，包含：

- 製造首頁與 25 項高頻工具表單（`web/`）
- OpenClaw Gateway 控制台整合（`/openclaw/`）
- 三項製造排程自動化（`automation/` + Cron）
- 大量製造場景技能（`skills/`）

## 快速開始

### 1) 啟動 Gateway（正式整合模式）

```bash
openclaw gateway restart
openclaw gateway status
```

開啟：

- `http://127.0.0.1:28789/` 或 `https://manuclaw.graceai.net/`：製造首頁
- `http://127.0.0.1:28789/openclaw/` 或 `https://manuclaw.graceai.net/openclaw/`：OpenClaw 控制台

### 2) 本機靜態預覽（僅 UI）

```bash
cd web
python3 -m http.server 8080
```

> 此模式只預覽網頁，不含 `/openclaw/` 控制台與 Gateway 能力。

## 專案結構

```text
.
├── web/                     # 製造業入口網站與 25 頁工具
├── automation/              # 自動化輸入/輸出/提示詞與文件
├── scripts/                 # 排程安裝腳本等
├── skills/                  # 製造、品質、供應鏈等技能庫
└── .openclaw/extensions/    # manufacturing-portal 插件
```

## 自動化排程（Cron）

已定義三個預設排程（Asia/Taipei）：

- 每天 07:30：班次交接摘要（`manufacturing-shift-handoff`）
- 每天 08:00：設備保養提醒（`equipment-maintenance-log`）
- 每週一 09:00：倉儲週報（`warehouse-reports`）

安裝/重裝排程：

```bash
./scripts/setup-manufacturing-cron.sh
```

管理常用指令：

```bash
openclaw cron list
openclaw cron run <job-id>
openclaw cron runs --id <job-id>
openclaw cron disable <job-id>
```

## 重要路由

- `/`：製造首頁
- `/pages/*`：各工具頁
- `/assets/*`：CSS/JS/圖片
- `/openclaw/`：OpenClaw 控制台

## 常見問題

- **首頁無樣式（像沒設計）**  
  先確認資源可讀：

  ```bash
  curl -I http://127.0.0.1:28789/assets/css/style.css
  ```

  若非 200，重啟 Gateway：

  ```bash
  openclaw gateway restart
  ```

- **對外網域仍顯示舊畫面**  
  可能是 CDN/瀏覽器快取，請強制重新整理（`Cmd+Shift+R`）。

## 相關文件

- 網站說明：`web/README.md`
- 自動化說明：`automation/README.md`

