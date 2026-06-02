# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## LemonTwin 果園（LemonTwin 專案）

| 項目 | 值 |
|------|-----|
| 專案路徑 | `/Users/joycechen/LemonTwin` |
| API（本機） | `http://127.0.0.1:3001/api` |
| API（tunnel） | `https://orchard.graceai.net/api` |
| Web | `https://orchard.graceai.net` |
| Farm ID | `demo-farm` |
| Demo 帳號 | `inspector@lemontwin.test` / `demo1234` |

環境變數（可寫入 `~/.openclaw/workspace/.env` 或 shell profile）：

```bash
export LEMONTWIN_API_BASE="http://127.0.0.1:3001/api"
export LEMONTWIN_FARM_ID="demo-farm"
export LEMONTWIN_EMAIL="inspector@lemontwin.test"
export LEMONTWIN_PASSWORD="demo1234"
```

OpenClaw skills：`lemontwin-api`、`lemontwin-daily-briefing`、`lemontwin-weather-duty`、`lemontwin-harvest`、`lemontwin-cameras`、`lemontwin-finance`、`orchard-shift-handoff`

腳本：`skills/lemontwin-api/scripts/lemontwin.sh`

派工規則：緊急樹勢→陳大明；天氣/監控→當日值班。

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)
