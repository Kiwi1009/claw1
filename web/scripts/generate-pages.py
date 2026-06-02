#!/usr/bin/env python3
"""Generate manufacturing tool pages from manifest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "pages"

PAGES = {
    "quotation": {
        "title": "專業報價單",
        "desc": "產出含單號、客戶、品項與貿易條款的報價草案。",
        "icon": "💰",
        "form": """
          <div class="form-row"><div class="form-group"><label>報價單號</label><input id="qtNo" /></div>
          <div class="form-group"><label>客戶公司</label><input id="customer" required /></div></div>
          <div class="form-group"><label>品項（每行：品名,數量,單價）</label><textarea id="lines" rows="6">軸承A,100,85\\n螺栓B,500,12</textarea></div>
          <div class="form-row"><div class="form-group"><label>幣別</label><select id="cur"><option>TWD</option><option>USD</option></select></div>
          <div class="form-group"><label>交期</label><input id="lead" placeholder="30 天" /></div></div>
          <div class="form-group"><label>Incoterms</label><input id="inco" value="FOB" /></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const lines=$("lines").value.split("\\n").filter(Boolean).map(l=>{const p=l.split(/[,，]/);return{品名:p[0],數量:p[1],單價:p[2]};});
            const total=lines.reduce((s,x)=>s+(+x.數量||0)*(+x.單價||0),0);
            showOutput("output",["=== 報價單草案 ===",`單號：${$("qtNo").value||"QT-"+Date.now()}`,`客戶：${$("customer").value}`,`幣別：${$("cur").value}`,`交期：${$("lead").value}`,`條款：${$("inco").value}`,"","品項:",...lines.map((x,i)=>`${i+1}. ${x.品名} x${x.數量} @${x.單價}`),`\\n總計：${total.toFixed(2)}`].join("\\n"));
          };
        """,
    },
    "cnc-quote": {
        "title": "CNC 加工報價",
        "desc": "依材質、工時與數量估算加工費與風險提示。",
        "icon": "⚙️",
        "form": """
          <div class="form-group"><label>零件名稱／圖號</label><input id="part" /></div>
          <div class="form-row"><div class="form-group"><label>材質</label><input id="mat" value="6061-T6" /></div>
          <div class="form-group"><label>數量</label><input type="number" id="qty" value="100" /></div></div>
          <div class="form-row"><div class="form-group"><label>預估工時(hr)</label><input type="number" id="hours" step="0.1" value="2.5" /></div>
          <div class="form-group"><label>機時費率</label><input type="number" id="rate" value="1200" /></div></div>
          <div class="form-group"><label>備註（薄壁、深孔等）</label><textarea id="risk"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const h=+$("hours").value,r=+$("rate").value,q=+$("qty").value;
            const unit=(h*r)/q; const setup=h*r*0.15;
            showOutput("output",[`=== CNC 報價草案 ===`,`零件：${$("part").value}`,`材質：${$("mat").value}`,`數量：${q}`,`加工費/件：${unit.toFixed(2)}`,`開機費：${setup.toFixed(0)}`,`總價估算：${(unit*q+setup).toFixed(0)}`,$("risk").value?"風險："+$("risk").value:""].filter(Boolean).join("\\n"));
          };
        """,
    },
    "supplier-scorecard": {
        "title": "供應商評分卡",
        "desc": "多供應商交期、品質、價格加權評分。",
        "icon": "⭐",
        "form": """
          <div class="form-group"><label>供應商資料（每行：名稱,交期分,品質分,價格分,溝通分）</label>
          <textarea id="rows" rows="8">甲公司,85,92,78,80\\n乙公司,70,88,90,75\\n丙公司,95,80,65,70</textarea></div>
          <p style="font-size:0.8rem;color:var(--muted)">各項 0–100，加權：交期30% 品質35% 價格25% 溝通10%</p>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const rows=$("rows").value.split("\\n").map(l=>{const p=l.split(/[,，]/);return{name:p[0],d:+p[1],q:+p[2],p:+p[3],c:+p[4]};}).filter(r=>r.name);
            const scored=rows.map(r=>({...r,total:Math.round(r.d*0.3+r.q*0.35+r.p*0.25+r.c*0.1)})).sort((a,b)=>b.total-a.total);
            showOutput("output",["=== 供應商評分 ===",...scored.map((r,i)=>`${i+1}. ${r.name} 綜合${r.total} (交${r.d} 品${r.q} 價${r.p})`)].join("\\n"));
          };
        """,
    },
    "capa": {
        "title": "CAPA 矯正預防",
        "desc": "不符合項調查與矯正、預防措施草案。",
        "icon": "🛡️",
        "form": """
          <div class="form-group"><label>CAPA 編號</label><input id="id" /></div>
          <div class="form-group"><label>問題描述</label><textarea id="prob" required></textarea></div>
          <div class="form-group"><label>圍堵措施</label><textarea id="contain"></textarea></div>
          <div class="form-group"><label>根本原因（5 Why 摘要）</label><textarea id="rc"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["# CAPA 草案",`編號：${$("id").value||"CAPA-"+Date.now()}`,`問題：${$("prob").value}`,`圍堵：${$("contain").value||"待填"}`,`根因：${$("rc").value||"待分析"}`,`矯正：`,`預防：`,`有效性驗證：待填`].join("\\n"));
          };
        """,
    },
    "kaizen-a3": {
        "title": "改善提案 A3",
        "desc": "A3 一頁式改善報告架構。",
        "icon": "💡",
        "form": """
          <div class="form-group"><label>主題</label><input id="topic" required /></div>
          <div class="form-group"><label>背景／問題</label><textarea id="bg"></textarea></div>
          <div class="form-group"><label>現況</label><textarea id="current"></textarea></div>
          <div class="form-group"><label>目標</label><textarea id="goal"></textarea></div>
          <div class="form-group"><label>對策</label><textarea id="action"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["# A3 改善提案",`主題：${$("topic").value}`,`背景：${$("bg").value}`,`現況：${$("current").value}`,`目標：${$("goal").value}`,`對策：${$("action").value}`,`追蹤：待填`].join("\\n"));
          };
        """,
    },
    "cad-review": {
        "title": "圖面審閱摘要",
        "desc": "登錄圖號與關鍵尺寸檢查項目。",
        "icon": "📐",
        "form": """
          <div class="form-group"><label>圖號</label><input id="dwg" required /></div>
          <div class="form-group"><label>關鍵尺寸（每行一項）</label><textarea id="dims" rows="6"></textarea></div>
          <div class="form-group"><label>審圖意見</label><textarea id="notes"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const dims=$("dims").value.split("\\n").filter(Boolean);
            showOutput("output",["=== 圖面審閱 ===",`圖號：${$("dwg").value}`,`審閱：${formatDate()}`,...dims.map((d,i)=>`尺寸${i+1}: ${d}`),`意見：${$("notes").value||"無"}`].join("\\n"));
          };
        """,
    },
    "incident-fupan": {
        "title": "產線事故復盤",
        "desc": "時間線、5 Why 與防再發行動。",
        "icon": "⚠️",
        "form": """
          <div class="form-group"><label>事故標題</label><input id="title" required /></div>
          <div class="form-group"><label>時間線</label><textarea id="timeline" rows="4"></textarea></div>
          <div class="form-group"><label>影響（停線、產量、客戶）</label><textarea id="impact"></textarea></div>
          <div class="form-group"><label>5 Why</label><textarea id="why" rows="4"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["# 事故復盤",`標題：${$("title").value}`,`時間：${formatDate()}`,`時間線：${$("timeline").value}`,`影響：${$("impact").value}`,`5 Why：${$("why").value}`,`改善：`,`防再發規則：`].join("\\n"));
          };
        """,
    },
    "predictive-maintenance": {
        "title": "預測性維護分析",
        "desc": "感測趨勢與停機紀錄維護建議。",
        "icon": "📡",
        "form": """
          <div class="form-group"><label>設備</label><input id="eq" required /></div>
          <div class="form-group"><label>感測趨勢說明</label><textarea id="sensor"></textarea></div>
          <div class="form-group"><label>近期停機（每行：日期,分鐘,原因）</label><textarea id="down" rows="4"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["=== 預測性維護 ===",`設備：${$("eq").value}`,`趨勢：${$("sensor").value}`,`停機紀錄：${$("down").value}`,`建議：安排預防保養窗口，優先檢查異常感測點`,`風險等級：中（請依實際數據調整）`].join("\\n"));
          };
        """,
    },
    "fjsp-repair": {
        "title": "排程修復 FJSP",
        "desc": "記錄排程衝突與修復建議。",
        "icon": "🧩",
        "form": """
          <div class="form-group"><label>衝突工單（每行：工單,原交期,衝突原因）</label><textarea id="conflicts" rows="6"></textarea></div>
          <div class="form-group"><label>政策限制說明</label><textarea id="policy"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["=== FJSP 排程修復 ===",$("conflicts").value.split("\\n").map((l,i)=>`${i+1}. ${l}`).join("\\n"),`政策：${$("policy").value||"—"}`,`建議：延後低優先工單、加班瓶頸站、拆批`].join("\\n\\n"));
          };
        """,
    },
    "iso-audit": {
        "title": "ISO 9001 內稽",
        "desc": "條款檢查與不符合風險。",
        "icon": "✅",
        "form": """
          <div class="form-group"><label>稽核範圍／程序</label><input id="scope" /></div>
          <div class="form-group"><label>條款檢查（每行：條款,狀態,備註）</label><textarea id="clauses" rows="8">8.5.1,符合,\\n8.5.2,觀察,標籤可追溯性待加強</textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["=== ISO 9001 內稽檢查表 ===",`範圍：${$("scope").value}`,`日期：${formatDate()}`,$("clauses").value].join("\\n"));
          };
        """,
    },
    "bom-analyzer": {
        "title": "BOM 報價比對",
        "desc": "多供應商料號對齊摘要。",
        "icon": "🔗",
        "form": """
          <div class="form-group"><label>專案名稱</label><input id="proj" /></div>
          <div class="form-group"><label>BOM 行（每行：料號,品名,供應商A價,供應商B價）</label><textarea id="bom" rows="8"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const rows=$("bom").value.split("\\n").filter(Boolean);
            showOutput("output",["=== BOM 比對 ===",`專案：${$("proj").value}`,...rows.map(r=>{const p=r.split(/[,，]/);const a=+p[2],b=+p[3];return`${p[0]} ${p[1]} | A:${a} B:${b} ${a<b?"→選A":"→選B"}`;})].join("\\n"));
          };
        """,
    },
    "heat-treatment": {
        "title": "熱處理製程建議",
        "desc": "材質、硬度與表面處理路線。",
        "icon": "🔥",
        "form": """
          <div class="form-group"><label>材質</label><input id="mat" value="SKD11" /></div>
          <div class="form-group"><label>硬度要求</label><input id="hard" value="HRC 58-62" /></div>
          <div class="form-group"><label>環境／耐蝕需求</label><input id="env" /></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",[`=== 製程建議 ===`,`材質：${$("mat").value}`,`硬度：${$("hard").value}`,`建議路線：淬火+回火 → 磨削 → 表面處理（依${$("env").value||"一般"}環境選鍍/陽極）`,`檢驗：硬度、金相、尺寸`].join("\\n"));
          };
        """,
    },
    "defect-codebook": {
        "title": "缺陷碼標準化",
        "desc": "自由文字對照標準 codebook。",
        "icon": "🏷️",
        "form": """
          <div class="form-group"><label>原始備註（每行一筆）</label><textarea id="raw" rows="6">刮傷嚴重\\nsize NG\\n焊點虛焊</textarea></div>
          <div class="form-group"><label>Codebook 參考（代碼:說明，每行）</label><textarea id="book" rows="5">SCR-01:表面刮傷\\nDIM-02:尺寸超差\\nSOL-03:焊接不良</textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            const book={};$("book").value.split("\\n").forEach(l=>{const[k,...v]=l.split(/[:：]/);if(k)book[k.trim()]=v.join(":").trim();});
            const map={刮:"SCR-01",size:"DIM-02",焊:"SOL-03",虛:"SOL-03"};
            const out=$("raw").value.split("\\n").map(r=>{const k=Object.keys(map).find(x=>r.includes(x));return`${r} → ${k?book[map[k]]||map[k]:"待人工對照"}`;});
            showOutput("output",out.join("\\n"));
          };
        """,
    },
    "defect-ai": {
        "title": "外觀不良初篩",
        "desc": "登錄影像檢驗結果與嚴重度。",
        "icon": "👁️",
        "form": """
          <div class="form-group"><label>批號／工單</label><input id="lot" /></div>
          <div class="form-group"><label>缺陷類型</label><select id="type"><option>刮傷</option><option>毛邊</option><option>色差</option><option>凹陷</option><option>異物</option></select></div>
          <div class="form-row"><div class="form-group"><label>嚴重度</label><select id="sev"><option>輕微</option><option>中等</option><option>嚴重</option></select></div>
          <div class="form-group"><label>位置說明</label><input id="loc" /></div></div>
          <div class="form-group"><label>備註</label><textarea id="note"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["=== 外觀檢驗紀錄 ===",`批號：${$("lot").value}`,`類型：${$("type").value}`,`嚴重度：${$("sev").value}`,`位置：${$("loc").value}`,`判定：${$("sev").value==="嚴重"?"隔離":"複判"}`,`備註：${$("note").value}`].join("\\n"));
          };
        """,
    },
    "consulting-report": {
        "title": "主管週報簡報",
        "desc": "KPI、異常與改善專案週報大綱。",
        "icon": "📈",
        "form": """
          <div class="form-group"><label>週次</label><input id="week" placeholder="2025-W21" /></div>
          <div class="form-group"><label>KPI 摘要</label><textarea id="kpi" rows="3"></textarea></div>
          <div class="form-group"><label>本週異常</label><textarea id="issues"></textarea></div>
          <div class="form-group"><label>下週重點</label><textarea id="next"></textarea></div>
        """,
        "script": """
          $("form").onsubmit=e=>{e.preventDefault();
            showOutput("output",["# 製造週報大綱",`週次：${$("week").value}`,`## KPI`,$("kpi").value,`## 異常`,$("issues").value,`## 下週重點`,$("next").value].join("\\n"));
          };
        """,
    },
}

HEADER = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} · OpenClaw 製造</title>
  <link rel="stylesheet" href="/assets/css/style.css?v=2" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo"><span class="logo-mark">{icon}</span> Open<span>Claw</span> 製造</a>
      <nav class="header-nav">
        <a href="/" class="nav-link">首頁</a>
        <a href="/openclaw/" class="btn btn-glow">OpenClaw 控制台</a>
      </nav>
    </div>
  </header>
  <main class="container">
    <div class="page-hero">
      <h1>{title}</h1>
      <p class="page-desc">{desc}</p>
    </div>
    <div class="layout-two">
      <div class="panel">
        <h3>輸入</h3>
        <form id="form">{form}
          <button type="submit" class="btn" style="margin-top:0.5rem">產出草案</button>
        </form>
      </div>
      <div class="panel">
        <h3>輸出草案</h3>
        <pre class="output-box" id="output">填寫後按「產出草案」</pre>
        <div class="output-actions">
          <button type="button" class="btn btn-secondary" onclick="copyOutput('output')">複製</button>
          <button type="button" class="btn btn-secondary" onclick="downloadOutput('output','{slug}.txt')">下載</button>
        </div>
      </div>
    </div>
  </main>
  <script src="/assets/css/style.css"></script>
  <script src="/assets/js/common.js"></script>
  <script>{script}</script>
</body>
</html>
'''

# fix wrong script tag in template
HEADER = HEADER.replace(
    '<script src="/assets/css/style.css"></script>',
    "",
)

for slug, cfg in PAGES.items():
    html = HEADER.format(slug=slug, **cfg)
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
    print("wrote", slug)
