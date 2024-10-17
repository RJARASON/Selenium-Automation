const http = require("http");
const fs = require("fs");
const path = require("path");

async function Http(folderPath) {
  const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, folderPath, req.url === "/" ? "index.html" : req.url);

    // Set the content type based on the file extension
    let extname = String(path.extname(filePath)).toLowerCase();
    const mimeTypes = {
      ".html": "text/html",
      ".js": "text/javascript",
      ".css": "text/css",
      ".json": "application/json",
      ".png": "image/png",
      ".jpg": "image/jpg",
      ".gif": "image/gif",
      ".wav": "audio/wav",
      ".mp4": "video/mp4",
      ".woff": "application/font-woff",
      ".ttf": "application/font-ttf",
      ".eot": "application/vnd.ms-fontobject",
      ".otf": "application/font-otf",
      ".svg": "application/image/svg+xml"
    };

    let contentType = mimeTypes[extname] || "application/octet-stream";

    fs.readFile(filePath, (err, data) => {
      if (err) {
        if (err.code === "ENOENT") {
          res.statusCode = 404;
          res.setHeader("Content-Type", "text/html");
          res.end("<h1>404 Not Found</h1>");
        } else {
          res.statusCode = 500;
          res.setHeader("Content-Type", "text/plain");
          res.end("Internal Server Error");
        }
      } else {
        res.statusCode = 200;
        res.setHeader("Content-Type", contentType);
        res.end(data);
      }
    });
  });

  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
  });
}

Http("ussd");
