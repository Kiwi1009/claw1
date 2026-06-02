import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DEFAULT_WEB_ROOT = path.resolve(__dirname, "../../../web");

const SKIP_PREFIXES = [
  "/openclaw",
  "/api",
  "/plugins",
  "/__openclaw",
  "/health",
  "/healthz",
  "/ready",
  "/readyz",
];

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".ico": "image/x-icon",
};

function resolveWebRoot(config) {
  const custom = config?.webRoot;
  if (custom && typeof custom === "string") {
    return path.resolve(custom);
  }
  return DEFAULT_WEB_ROOT;
}

function safeFilePath(root, urlPath) {
  let rel = decodeURIComponent(urlPath);
  if (rel === "/" || rel === "") rel = "index.html";
  else rel = rel.replace(/^\//, "");
  rel = path.normalize(rel);
  if (rel.startsWith("..") || path.isAbsolute(rel)) return null;
  const filePath = path.join(root, rel);
  const rootReal = fs.realpathSync(root);
  let fileReal;
  try {
    fileReal = fs.realpathSync(filePath);
  } catch {
    return null;
  }
  if (!fileReal.startsWith(rootReal + path.sep) && fileReal !== rootReal) return null;
  return fileReal;
}

function serveFile(req, res, filePath) {
  const ext = path.extname(filePath).toLowerCase();
  if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) return false;
  if (req.method === "HEAD") {
    res.statusCode = 200;
    res.setHeader("Content-Type", MIME[ext] || "application/octet-stream");
    res.end();
    return true;
  }
  if (req.method !== "GET") return false;
  res.statusCode = 200;
  res.setHeader("Content-Type", MIME[ext] || "application/octet-stream");
  res.setHeader("Cache-Control", "no-cache");
  fs.createReadStream(filePath).pipe(res);
  return true;
}

/** Gateway prefix "/" only matches the root path, not /assets or /pages. */
const STATIC_ROUTE_PREFIXES = ["/", "/assets", "/pages"];

export default definePluginEntry({
  id: "manufacturing-portal",
  name: "Manufacturing Portal",
  description: "Manufacturing homepage and tools at /",
  register(api) {
    const webRoot = resolveWebRoot(api.pluginConfig);

    const handler = async (req, res) => {
      const url = new URL(req.url || "/", "http://localhost");
      const { pathname } = url;
      if (SKIP_PREFIXES.some((p) => pathname === p || pathname.startsWith(`${p}/`))) {
        return false;
      }
      if (!["GET", "HEAD"].includes(req.method || "GET")) return false;
      let filePath;
      try {
        filePath = safeFilePath(webRoot, pathname);
      } catch {
        res.statusCode = 404;
        res.end("Not Found");
        return true;
      }
      if (!filePath || !serveFile(req, res, filePath)) {
        res.statusCode = 404;
        res.setHeader("Content-Type", "text/plain; charset=utf-8");
        res.end("Not Found");
        return true;
      }
      return true;
    };

    for (const routePath of STATIC_ROUTE_PREFIXES) {
      api.registerHttpRoute({
        path: routePath,
        match: "prefix",
        auth: "plugin",
        replaceExisting: routePath === "/",
        handler,
      });
    }

    api.logger.info?.(
      `[manufacturing-portal] serving ${webRoot} at /, /assets, /pages (OpenClaw UI: /openclaw/)`,
    );
  },
});
