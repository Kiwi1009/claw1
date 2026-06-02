---
name: create-dxf
description: 從自然語言設計提示衍生的嚴格、已驗證的 JSON 規格生成符合報價需求的 2D DXF（以及可選的 SVG 預覽）文件。此功能適用於板材/板件零件（水刀/雷射/路由器），如安裝板、襯板、支架、孔位圖案和槽口。
---

# create-dxf

Deterministically generate a **manufacturing-friendly DXF** from a small JSON spec (center-origin, explicit units). Also emits an SVG preview.

## Quick start

1) Convert prompt → JSON (see `references/spec_schema.md`).
2) Validate:

```bash
python3 scripts/create_dxf.py validate spec.json
```

3) Render:

```bash
python3 scripts/create_dxf.py render spec.json --outdir out
```

Outputs:
- `out/<name>.dxf`
- `out/<name>.svg`

## Notes

- DXF uses simple entities for compatibility: closed `LWPOLYLINE` outer profile + `CIRCLE` holes.
- Default layers are manufacturing-oriented:
  - `CUT_OUTER` (outer perimeter)
  - `CUT_INNER` (holes/slots)
  - `NOTES` (optional)

## Resources

- `scripts/create_dxf.py`
- `references/spec_schema.md`
- `references/test_prompts.md`
