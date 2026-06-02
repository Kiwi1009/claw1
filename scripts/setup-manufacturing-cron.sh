#!/usr/bin/env bash
# 註冊三項製造業 Cron 任務（需 Gateway 運行中）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROMPTS="$ROOT/automation/prompts"
TZ="${OPENCLAW_CRON_TZ:-Asia/Taipei}"

msg() { cat "$PROMPTS/$1"; }

echo "→ 檢查 Gateway…"
openclaw gateway status >/dev/null 2>&1 || {
  echo "請先啟動 Gateway: openclaw gateway"
  exit 1
}

mkdir -p "$ROOT/automation/outputs"

add_job() {
  local name="$1" cron_expr="$2" prompt_file="$3"
  echo "→ 新增：$name ($cron_expr $TZ)"
  openclaw cron add \
    --name "$name" \
    --cron "$cron_expr" \
    --tz "$TZ" \
    --session isolated \
    --timeout-seconds 600 \
    --no-deliver \
    --message "$(msg "$prompt_file")"
}

# 避免重複：若同名 job 已存在則略過
for existing in "製造-每日班次交接" "製造-每週倉儲週報" "製造-每日設備保養"; do
  if openclaw cron list 2>/dev/null | grep -q "$existing"; then
    echo "已存在：$existing（略過）"
  fi
done

if ! openclaw cron list 2>/dev/null | grep -q "製造-每日班次交接"; then
  add_job "製造-每日班次交接" "30 7 * * *" "daily-shift-handoff.txt"
fi

if ! openclaw cron list 2>/dev/null | grep -q "製造-每週倉儲週報"; then
  add_job "製造-每週倉儲週報" "0 9 * * 1" "weekly-warehouse.txt"
fi

if ! openclaw cron list 2>/dev/null | grep -q "製造-每日設備保養"; then
  add_job "製造-每日設備保養" "0 8 * * *" "daily-maintenance.txt"
fi

echo ""
echo "完成。目前排程："
openclaw cron list
