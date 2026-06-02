const CAT_COLORS = {
  現場: { color: "#059669", bg: "#ecfdf5" },
  品質: { color: "#7c3aed", bg: "#f5f3ff" },
  生管: { color: "#2563eb", bg: "#eff6ff" },
  供應鏈: { color: "#d97706", bg: "#fffbeb" },
  設備: { color: "#0891b2", bg: "#ecfeff" },
  業務: { color: "#db2777", bg: "#fdf2f8" },
  工程: { color: "#4f46e5", bg: "#eef2ff" },
  改善: { color: "#16a34a", bg: "#f0fdf4" },
  管理: { color: "#64748b", bg: "#f8fafc" },
};

function renderFeatured() {
  const row = document.getElementById("featured-row");
  if (!row || typeof MANUFACTURING_TOOLS === "undefined") return;
  MANUFACTURING_TOOLS.slice(0, 5).forEach((t) => {
    const a = document.createElement("a");
    a.href = `/pages/${t.slug}.html`;
    a.className = "featured-card";
    a.innerHTML = `
      <span class="fc-icon">${t.icon}</span>
      <span class="fc-rank">#${t.rank}</span>
      <span class="fc-name">${t.name}</span>
    `;
    row.appendChild(a);
  });
}

function renderHomepage() {
  const grid = document.getElementById("tools-root");
  if (!grid || typeof MANUFACTURING_TOOLS === "undefined") return;

  const byCat = {};
  MANUFACTURING_TOOLS.forEach((t) => {
    if (!byCat[t.cat]) byCat[t.cat] = [];
    byCat[t.cat].push(t);
  });

  CATEGORY_ORDER.filter((c) => c === "全部" || byCat[c]).forEach((cat) => {
    if (cat === "全部") return;
    const section = document.createElement("section");
    section.className = "category-section";
    section.dataset.category = cat;
    const count = byCat[cat].length;
    section.innerHTML = `
      <h2 class="category-title">
        ${cat}
        <span class="category-count">${count} 項</span>
      </h2>
      <div class="tools-grid"></div>
    `;
    const inner = section.querySelector(".tools-grid");
    byCat[cat].forEach((t) => inner.appendChild(createToolCard(t)));
    grid.appendChild(section);
  });

  const search = document.getElementById("tool-search");
  const chips = document.querySelectorAll(".filter-chips .chip");
  const empty = document.getElementById("empty-state");
  const resultCount = document.getElementById("result-count");
  let activeCat = "全部";

  function applyFilter() {
    const q = (search?.value || "").trim().toLowerCase();
    let visible = 0;
    document.querySelectorAll(".tool-card").forEach((card) => {
      const matchCat = activeCat === "全部" || card.dataset.cat === activeCat;
      const matchQ =
        !q ||
        card.dataset.name.includes(q) ||
        card.dataset.desc.includes(q) ||
        card.dataset.rank.includes(q);
      const show = matchCat && matchQ;
      card.classList.toggle("hidden", !show);
      if (show) visible++;
    });
    document.querySelectorAll(".category-section").forEach((sec) => {
      const n = sec.querySelectorAll(".tool-card:not(.hidden)").length;
      sec.classList.toggle("hidden", n === 0);
    });
    if (empty) empty.classList.toggle("hidden", visible > 0);
    if (resultCount) {
      resultCount.textContent =
        visible === MANUFACTURING_TOOLS.length
          ? `共 ${visible} 項`
          : `顯示 ${visible} / ${MANUFACTURING_TOOLS.length} 項`;
    }
  }

  search?.addEventListener("input", applyFilter);
  chips.forEach((chip) => {
    chip.addEventListener("click", () => {
      chips.forEach((c) => c.classList.remove("active"));
      chip.classList.add("active");
      activeCat = chip.dataset.cat || "全部";
      applyFilter();
    });
  });
  applyFilter();
}

function createToolCard(t) {
  const art = document.createElement("article");
  art.className = "tool-card";
  art.dataset.cat = t.cat;
  art.dataset.name = t.name.toLowerCase();
  art.dataset.desc = t.desc.toLowerCase();
  art.dataset.rank = String(t.rank);
  const freqClass =
    t.freq === "daily" ? "badge-daily" : t.freq === "weekly" ? "badge-weekly" : "badge-event";
  const freqLabel =
    t.freq === "daily" ? "高頻使用" : t.freq === "weekly" ? "週期性" : "事件觸發";
  const c = CAT_COLORS[t.cat] || { color: "#2563eb", bg: "#eff6ff" };
  art.style.setProperty("--cat-color", c.color);
  art.style.setProperty("--cat-bg", c.bg);

  art.innerHTML = `
    <div class="tool-card-accent"></div>
    <div class="tool-card-body">
      <div class="tool-card-top">
        <div class="tool-icon-wrap">${t.icon}</div>
        <div class="tool-card-meta">
          <span class="tool-rank">使用率排名 #${t.rank}</span>
          <h3>${t.name}</h3>
        </div>
      </div>
      <p>${t.desc}</p>
      <div class="tool-card-footer">
        <span class="badge ${freqClass}">${freqLabel}</span>
        <a class="btn-open" href="/pages/${t.slug}.html">開啟 →</a>
      </div>
    </div>
  `;
  art.addEventListener("click", (e) => {
    if (e.target.closest("a")) return;
    window.location.href = `/pages/${t.slug}.html`;
  });
  art.style.cursor = "pointer";
  return art;
}

document.addEventListener("DOMContentLoaded", () => {
  renderFeatured();
  renderHomepage();
});
