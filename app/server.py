from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from app.db import get_val


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        path = urlparse(self.path).path

        if path == "/health":
            self._send_json(200, {"ok": True})
            return

        if path.startswith("/vals/"):
            try:
                val_id = int(path.removeprefix("/vals/"))
                self._send_json(200, get_val(val_id))
            except Exception as exc:
                self._send_json(500, {"error": str(exc)})
            return

        self._send_json(404, {"error": "not found"})

    def _send_json(self, status: int, body: dict[str, object]) -> None:
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("listening on http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
