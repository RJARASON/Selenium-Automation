const http = require("http");
const fs = require("fs");
const path = require("path");

async function Http(filepath) {
  const server = http.createServer((req, res) => {
    if (req.url === "/") {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/html");
      res.end("You are in the server\n: USE this url to navigate to the index : http://localhost:3000Index\n");
    } else if (req.url === "/Index") {
      const filePath = path.join(__dirname, filepath);
      fs.readFile(filePath, (err, data) => {
        if (err) {
          res.statusCode = 500;
          res.setHeader("Content-Type", "text/plain");
          res.end("Internal Server Error\n");
        } else {
          res.statusCode = 200;
          res.setHeader("Content-Type", "text/html");
          res.end(data);
        }
      });
    } else {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/html");
      res.end("404 Not Found\n");
    }
  });

  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}Index`);
  });
}

Http("index.html")