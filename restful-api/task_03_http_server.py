#!/usr/bin/env/python3
"""A simple HTTP server with multiple endpoints."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler with multiple endpoints.

    Endpoints:
        /          : Returns a welcome message.
        /data      : Returns a JSON object with sample data.
        /status    : Returns a plain text "OK" message.
        Any other path : Returns a 404 Not Found message.
    """
    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/" or self.path == "":     # Root path
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":  # Data path
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":    # Status path
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":  # Info path
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"version": "1.0", "description": "A simple API built with http.server"}).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print(f"Serving at {PORT}...")
    httpd.serve_forever()
