#!/usr/bin/env python3
import http.server
import socketserver
import os

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set content type for files without extension
        if self.path == '/loading':
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

    def do_GET(self):
        # Handle /loading route without .html extension
        if self.path == '/loading':
            self.path = '/loading.html'
        super().do_GET()

PORT = 8000

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Access your loading page at: http://localhost:{PORT}/loading")
    httpd.serve_forever() 