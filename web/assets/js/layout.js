/** 功能頁共用頁首（由各頁在 body 開頭呼叫） */
function renderPageHeader(title) {
  const header = document.querySelector(".site-header .header-inner");
  if (!header || header.dataset.enhanced) return;
  header.dataset.enhanced = "1";
  const nav = header.querySelector(".header-nav");
  if (nav && !nav.querySelector(".nav-link")) {
    const home = document.createElement("a");
    home.href = "/";
    home.className = "nav-link";
    home.textContent = "首頁";
    nav.insertBefore(home, nav.firstChild);
  }
  if (title && document.querySelector(".page-hero h1")) {
    document.title = `${title} · OpenClaw 製造`;
  }
}
