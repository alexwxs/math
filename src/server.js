import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const publicDir = path.join(root, "public");

const PORT = Number(process.env.PORT) || 2026;

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
  ".ico": "image/x-icon",
};

function send(res, status, body, headers = {}) {
  res.writeHead(status, headers);
  res.end(body);
}

function sendFile(res, filePath) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      send(res, 404, "Not found", { "Content-Type": "text/plain; charset=utf-8" });
      return;
    }
    const ext = path.extname(filePath).toLowerCase();
    send(res, 200, data, {
      "Content-Type": TYPES[ext] || "application/octet-stream",
      "Cache-Control":
        ext === ".html" || ext === ".css" || ext === ".js" || ext === ".png"
          ? "no-cache"
          : "public, max-age=3600",
    });
  });
}

const homePage = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Math</title>
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <header class="top">
    <a class="brand" href="/">Math</a>
    <nav>
      <a href="/year7/">Year 7</a>
      <a href="/year11/">Year 11</a>
      <a href="/year12/">Year 12</a>
    </nav>
  </header>
  <main class="page home">
    <h1>Math</h1>
    <p>Questions and worked solutions.</p>
    <p class="home-links">
      <a class="cta" href="/year7/">Open Year 7</a>
      <a class="cta cta-secondary" href="/year11/">Open Year 11</a>
      <a class="cta cta-secondary" href="/year12/">Open Year 12</a>
    </p>
  </main>
</body>
</html>`;

function redirectYear(pathname, res) {
  if (pathname === "/year7") {
    res.writeHead(302, { Location: "/year7/" });
    res.end();
    return true;
  }
  if (pathname === "/year11") {
    res.writeHead(302, { Location: "/year11/" });
    res.end();
    return true;
  }
  if (pathname === "/year12") {
    res.writeHead(302, { Location: "/year12/" });
    res.end();
    return true;
  }
  return false;
}

const server = http.createServer((req, res) => {
  try {
    let pathname;
    try {
      const raw = req.url || "/";
      // Protocol-relative paths like "//" break URL parsing; normalise first.
      const pathOnly = raw.startsWith("//") ? `/${raw.replace(/^\/+/, "")}` : raw;
      const url = new URL(pathOnly, `http://${req.headers.host || "localhost"}`);
      pathname = decodeURIComponent(url.pathname);
    } catch {
      send(res, 400, "Bad request", { "Content-Type": "text/plain; charset=utf-8" });
      return;
    }

    // Reject null bytes / control chars from scanners before touching the filesystem.
    if (/[\0-\x1f]/.test(pathname)) {
      send(res, 400, "Bad request", { "Content-Type": "text/plain; charset=utf-8" });
      return;
    }

    if (pathname === "/") {
      send(res, 200, homePage, { "Content-Type": "text/html; charset=utf-8" });
      return;
    }

    if (redirectYear(pathname, res)) return;

    if (pathname === "/year7/") {
      sendFile(res, path.join(publicDir, "year7", "index.html"));
      return;
    }

    if (pathname === "/year11/") {
      sendFile(res, path.join(publicDir, "year11", "index.html"));
      return;
    }

    if (pathname === "/year12/") {
      sendFile(res, path.join(publicDir, "year12", "index.html"));
      return;
    }

    const safe = path.normalize(pathname).replace(/^(\.\.[/\\])+/, "");
    const filePath = path.join(publicDir, safe);
    if (!filePath.startsWith(publicDir) || /[\0-\x1f]/.test(filePath)) {
      send(res, 403, "Forbidden", { "Content-Type": "text/plain; charset=utf-8" });
      return;
    }
    fs.stat(filePath, (err, st) => {
      if (err || !st.isFile()) {
        send(res, 404, "Not found", { "Content-Type": "text/plain; charset=utf-8" });
        return;
      }
      sendFile(res, filePath);
    });
  } catch {
    if (!res.headersSent) {
      send(res, 400, "Bad request", { "Content-Type": "text/plain; charset=utf-8" });
    }
  }
});

server.on("clientError", (_err, socket) => {
  socket.end("HTTP/1.1 400 Bad Request\r\n\r\n");
});

server.listen(PORT, () => {
  console.log(`Math server listening on http://localhost:${PORT}`);
  console.log(`Year 7: http://localhost:${PORT}/year7/`);
  console.log(`Year 11: http://localhost:${PORT}/year11/`);
  console.log(`Year 12: http://localhost:${PORT}/year12/`);
});
