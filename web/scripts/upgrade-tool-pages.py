#!/usr/bin/env python3
"""Apply unified light theme shell to all tool pages."""
import re
from pathlib import Path

PAGES_DIR = Path(__file__).resolve().parent.parent / "pages"

HEADER_SVG = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>'''

SHELL_HEADER = f'''  <div class="app-bg" aria-hidden="true"></div>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo">
        <span class="logo-mark" aria-hidden="true">{HEADER_SVG}</span>
        <span class="logo-text">Open<span>Claw</span> 製造</span>
      </a>
      <nav class="header-nav">
        <a href="/" class="nav-link">← 首頁</a>
        <a href="/openclaw/" class="btn btn-primary">AI 控制台</a>
      </nav>
    </div>
  </header>
  <main class="container page-main">'''

FOOTER = '''
  <footer class="site-footer">
    <div class="container footer-inner">
      <a href="/">返回首頁</a>
      <span>·</span>
      <a href="/openclaw/">OpenClaw 控制台</a>
    </div>
  </footer>
'''

def extract_title(html):
    m = re.search(r"<title>([^<]+)</title>", html)
    if m:
        return m.group(1).replace(" · OpenClaw 製造", "").replace(" · OpenClaw", "").strip()
    return "工具"

def extract_desc(html):
    m = re.search(r'class="page-desc">([^<]+)</p>', html)
    if m:
        return m.group(1)
    m = re.search(r'class="page-desc">([^<]+)</p>', html) or re.search(r"<p class=\"page-desc\">([^<]+)", html)
    return m.group(1) if m else ""

def extract_h1(html):
    m = re.search(r'class="page-title">([^<]+)</h1>', html)
    if not m:
        m = re.search(r"<h1[^>]*>([^<]+)</h1>", html)
    return m.group(1) if m else extract_title(html)

def upgrade(path: Path):
    html = path.read_text(encoding="utf-8")
    title = extract_h1(html)
    desc = extract_desc(html)

    # body class
    html = re.sub(r"<body[^>]*>", '<body class="tool-page">', html, count=1)

    # Replace header through main start
    html = re.sub(
        r"<body class=\"tool-page\">.*?</header>\s*<main class=\"container[^\"]*\">",
        "<body class=\"tool-page\">" + SHELL_HEADER,
        html,
        count=1,
        flags=re.DOTALL,
    )

    # Fix page-hero with breadcrumb
    if "breadcrumb" not in html:
        html = re.sub(
            r'(<div class="page-hero">)\s*',
            r'\1\n      <p class="breadcrumb"><a href="/">首頁</a> / <span>' + re.escape(title.split("（")[0].split("(")[0][:20]) + "</span></p>\n      ",
            html,
            count=1,
        )

    # Mark output panel
    html = html.replace("<h3>輸出", '<h3 class="panel-output-title">輸出', 1)
    html = re.sub(
        r'(<div class="panel">\s*)<h3 class="panel-output-title">',
        r'<div class="panel panel-output">\n        <h3>',
        html,
        count=1,
    )
    # second panel with 輸出 in h3
    if "panel-output" not in html:
        parts = html.split('<div class="layout-two">', 1)
        if len(parts) == 2:
            rest = parts[1]
            idx = rest.rfind('<div class="panel">')
            if idx >= 0:
                rest = rest[:idx] + '<div class="panel panel-output">' + rest[idx + len('<div class="panel">'):]
                html = parts[0] + '<div class="layout-two">' + rest

    # output placeholder class
    html = re.sub(
        r'(<pre class="output-box" id="output">)([^<]*)',
        lambda m: m.group(1) + ('<span class="output-placeholder">' + m.group(2) + '</span>' if m.group(2).strip() and "placeholder" not in m.group(2) else m.group(2)),
        html,
        count=1,
    )

    # Add footer before scripts if missing
    if "site-footer" not in html:
        html = re.sub(
            r"(</main>)\s*(<script)",
            FOOTER + r"\n\1\n  \2",
            html,
            count=1,
        )

    # Submit button text consistency
    html = html.replace('class="btn" style="margin-top:0.5rem">產出草案', 'class="btn" style="margin-top:0.75rem">產出草案')

    path.write_text(html, encoding="utf-8")
    print("ok", path.name)

for p in sorted(PAGES_DIR.glob("*.html")):
    upgrade(p)
