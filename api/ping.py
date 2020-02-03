#!/usr/bin/env python3

import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'received': 'pong', 
            'status': 200,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
    return
