function $(id) {
  return document.getElementById(id);
}

function formatDate(d) {
  const x = d || new Date();
  return x.toLocaleString("zh-TW", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function showOutput(el, text) {
  if (typeof el === "string") el = $(el);
  if (!el) return;
  el.textContent = text;
  el.classList.remove("hidden");
  el.classList.remove("output-placeholder");
}

function copyOutput(id) {
  const el = $(id);
  if (!el || !el.textContent) return;
  navigator.clipboard.writeText(el.textContent).then(() => {
    alert("已複製到剪貼簿");
  });
}

function downloadOutput(id, filename) {
  const el = $(id);
  if (!el || !el.textContent) return;
  const blob = new Blob([el.textContent], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = filename || "openclaw-output.txt";
  a.click();
  URL.revokeObjectURL(a.href);
}

function parseLines(text) {
  return (text || "")
    .split("\n")
    .map((s) => s.trim())
    .filter(Boolean);
}

function mean(arr) {
  if (!arr.length) return 0;
  return arr.reduce((a, b) => a + b, 0) / arr.length;
}

function stdDev(arr) {
  if (arr.length < 2) return 0;
  const m = mean(arr);
  const v = arr.reduce((s, x) => s + (x - m) ** 2, 0) / (arr.length - 1);
  return Math.sqrt(v);
}

function parseNumbers(text) {
  return (text || "")
    .split(/[\s,;\t]+/)
    .map((s) => parseFloat(s.trim()))
    .filter((n) => !Number.isNaN(n));
}
