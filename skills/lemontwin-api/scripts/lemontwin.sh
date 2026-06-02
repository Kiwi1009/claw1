#!/usr/bin/env bash
# LemonTwin API helper — requires curl and jq
set -euo pipefail

BASE="${LEMONTWIN_API_BASE:-http://127.0.0.1:3001/api}"
FARM="${LEMONTWIN_FARM_ID:-demo-farm}"
EMAIL="${LEMONTWIN_EMAIL:-inspector@lemontwin.test}"
PASS="${LEMONTWIN_PASSWORD:-demo1234}"
TOKEN_FILE="${LEMONTWIN_TOKEN_FILE:-$HOME/.openclaw/workspace/.lemontwin-token}"

token() {
  if [[ -f "$TOKEN_FILE" ]]; then
    cat "$TOKEN_FILE"
    return
  fi
  local t
  t=$(curl -sf -X POST "$BASE/auth/login" \
    -H "Content-Type: application/json" \
    -d "{\"email\":\"$EMAIL\",\"password\":\"$PASS\"}" | jq -r '.token')
  echo "$t" > "$TOKEN_FILE"
  echo "$t"
}

auth() {
  echo "Authorization: Bearer $(token)"
}

cmd="${1:-help}"
shift || true

case "$cmd" in
  login)
    rm -f "$TOKEN_FILE"
    token > /dev/null
    echo "OK token saved to $TOKEN_FILE"
    ;;
  health)
    curl -sf "$BASE/health" | jq .
    ;;
  operations)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/operations" | jq .
    ;;
  weather-today)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/weather/today" | jq .
    ;;
  weather-evaluate)
    curl -sf -X POST -H "$(auth)" "$BASE/farms/$FARM/weather/evaluate" | jq .
    ;;
  tasks)
    curl -sf -H "$(auth)" "$BASE/tasks?farmId=$FARM" | jq .
    ;;
  dispatch)
    month="${1:-$(date +%-m)}"
    year="${2:-$(date +%Y)}"
    curl -sf -X POST -H "$(auth)" -H "Content-Type: application/json" \
      "$BASE/farms/$FARM/dispatch" \
      -d "{\"month\":$month,\"year\":$year}" | jq .
    ;;
  harvests)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/harvests" | jq .
    ;;
  finance)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/finance-summary" | jq .
    ;;
  cameras)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/cameras" | jq .
    ;;
  snapshot-all)
    curl -sf -X POST -H "$(auth)" "$BASE/farms/$FARM/cameras/snapshot-all" | jq .
    ;;
  trees)
    curl -sf -H "$(auth)" "$BASE/farms/$FARM/trees" | jq .
    ;;
  help|*)
    echo "Usage: lemontwin.sh <command>"
    echo "  login | health | operations | weather-today | weather-evaluate"
    echo "  tasks | dispatch [month] [year] | harvests | finance | cameras | snapshot-all | trees"
    echo "Env: LEMONTWIN_API_BASE LEMONTWIN_FARM_ID LEMONTWIN_EMAIL LEMONTWIN_PASSWORD"
    ;;
esac
