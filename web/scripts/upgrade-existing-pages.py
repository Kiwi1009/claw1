#!/usr/bin/env python3
from pathlib import Path

HEADER = '''  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo"><span class="logo-mark">⚙</span> Open<span>Claw</span> 製造</a>
      <nav class="header-nav">
        <a href="/" class="nav-link">首頁</a>
        <a href="/openclaw/" class="btn btn-glow">OpenClaw 控制台</a>
      </nav>
    </div>
  </header>
  <main class="container">
    <div class="page-hero">'''

OLD_SLUGS = [
    "mes-log", "shift-handoff", "purchase-record", "iqc", "spc",
    "production-schedule", "warehouse-report", "equipment-maintenance",
    "customer-response", "complaint-8d",
]

pages = Path(__file__).resolve().parent.parent / "pages"

for slug in OLD_SLUGS:
    p = pages / f"{slug}.html"
    text = p.read_text(encoding="utf-8")
    # wrap h1 in page-hero if needed
    if "page-hero" not in text:
        text = text.replace(
            '  <main class="container">\n    <h1 class="page-title">',
            '  <main class="container">\n    <div class="page-hero">\n      <h1 class="page-title">',
        )
        text = text.replace(
            '    <p class="page-desc">',
            '      <p class="page-desc">',
            1,
        )
        text = text.replace(
            '    <div class="layout-two">',
            '    </div>\n    <div class="layout-two">',
            1,
        )
    # replace header block
    import re
    text = re.sub(
        r'  <header class="site-header">.*?</header>\s*  <main class="container">\s*(?:<div class="page-hero">)?',
        HEADER,
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace('class="page-title"', 'class="page-title"')  # keep
    p.write_text(text, encoding="utf-8")
    print("upgraded", slug)
