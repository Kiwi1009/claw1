---
name: warehouse-chart-reports
description: 從 SQLite/CSV 資料生成倉儲分析圖表、表格圖像以及報告用視覺化圖形。當使用者要求倉儲圖表、產品表格圖像、庫存健康圓餅圖、營收/利潤視覺化、缺貨產品視覺化，或 PDF/投影片報告用圖像資產時，使用此功能。
---

# Warehouse Chart Reports

Use this skill to produce clean chart/report images for warehouse demos.

## Run full warehouse visual pack (recommended)

Execute:

```bash
python skills/warehouse-chart-reports/scripts/run_warehouse_reports.py \
  --db demo/warehouse_agent/warehouse_demo.db \
  --out demo/warehouse_agent/outputs
```

This generates:
- `stock_status_pie.png`
- `revenue_by_category.png`
- `daily_profit_30d.png`
- `product_table_top40.png`
- `missing_products.csv`
- `kpi_summary.txt`

## Generate product table image only

Execute:

```bash
python skills/warehouse-chart-reports/scripts/product_table_image.py \
  --db demo/warehouse_agent/warehouse_demo.db \
  --out demo/warehouse_agent/outputs/product_table_top40.png \
  --limit 40
```

## Notes

- Prefer virtualenv Python when matplotlib is unavailable system-wide.
- Keep chart style simple and readable for PDF embedding.
- If sales timestamps are sparse for today, use the 30-day profit chart for trend visibility.
