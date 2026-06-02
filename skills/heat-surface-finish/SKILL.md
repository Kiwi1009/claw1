---
name: "heat-surface-finish"
version: "1.0.0"
description: "熱處理 / 鍍膜 / 表面處理製程顧問。涵蓋退火、淬火、回火、滲碳、氮化、感應淬火、鍍鋅/鎳/鉻、陽極處理、鈍化、PVD/CVD 刀具塗層、粉體塗裝、電泳、硬度換算 (HRC/HV/HB)、常見缺陷與對應 ASTM/AMS/MIL 規範。當客戶提到「淬火/回火」「鍍鋅/三價鉻」「陽極氧化」「鈍化」「PVD/TiN/AlTiN」「硬度要求」「白層」「回火脆性」「鍍層剝離」等關鍵字時啟用。"
author: "joyce628"
tags: [heat-treatment, surface-finish, plating, anodizing, hardness, metal-machining, manufacturing]
category: "industrial"
---

# 🔥 Heat & Surface Finish — 金屬製程顧問

針對金屬加工廠常見的熱處理 + 表面處理工藝,提供參數對照、缺陷判讀、規範引用。

## When to Use

- 客戶圖紙標 HRC 硬度要求 → 選熱處理製程
- 鋼料調質 / 淬火裂 / 回火脆性 排查
- 滲碳 / 氮化 深度 / 硬度層 設計
- 不銹鋼鈍化、鋁件陽極、五金鍍鋅/三價鉻 製程選擇
- 刀具/模具 PVD 塗層挑選 (TiN/TiCN/AlTiN/DLC)
- 鍍層起泡、剝離、針孔、變色 缺陷分析
- 硬度單位換算 HRC ↔ HV ↔ HB ↔ HRB ↔ Rm

## Commands

| 指令 | 說明 |
|---|---|
| `scripts/script.sh intro` | 製程地圖 — 從圖紙要求反查該用什麼 |
| `scripts/script.sh anneal` | 退火 / 正火 / 應力消除 — 參數、爐冷/空冷 |
| `scripts/script.sh harden` | 淬火 + 回火 — S45C / SCM440 / SKD11 / SKD61 / SUS440C 參數 |
| `scripts/script.sh case` | 表面硬化 — 滲碳、氮化、氮碳共滲、感應淬火、火焰淬火 |
| `scripts/script.sh hardness` | HRC / HV / HB / HRB / Rm 換算表 + 應用 |
| `scripts/script.sh plating` | 鍍鋅 / 鍍鎳 / 鍍鉻 / 化學鍍鎳 / 三價鉻 |
| `scripts/script.sh anodize` | 鋁陽極 Type I/II/III + 染色 + 封孔 |
| `scripts/script.sh passivate` | 不銹鋼鈍化 / 酸洗 / 電解拋光 |
| `scripts/script.sh coatings` | PVD / CVD / DLC / TiN / AlTiN — 刀具與模具 |
| `scripts/script.sh paint` | 噴漆 / 粉體塗裝 / 電泳 |
| `scripts/script.sh defects` | 常見缺陷 — 淬火裂、白層、回火脆性、鍍層起泡 |
| `scripts/script.sh standards` | 規範引用 — ASTM / AMS / MIL / JIS / ISO |
| `scripts/script.sh all` | 一次列出所有章節 |

## How to invoke

直接讓 model 看到上述指令並用 bash 執行;或 user 在 chat 中問:「S45C 客戶要 HRC55,怎麼處理?」→ model 觸發 `harden` + `hardness` 章節。

## Sources

引用標準: ASTM A370 (硬度測試)、ASTM E140 (硬度換算)、ASTM B633 (鋅鍍)、ASTM B488 (金鍍)、AMS 2700 (鈍化)、MIL-A-8625 (鋁陽極)、ISO 4042 (扣件鍍)、JIS H 8610 (電鍍)、NADCAP AC7108 (熱處理)。
