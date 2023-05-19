from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _log_request_details(self):
        print(f"Request from: {self.client_address[0]}")
        print(f"Request method: {self.command}")
        print(f"Request path: {self.path}")
        print(f"Request headers:\n{self.headers}\n")

    def do_GET(self):
        self._log_request_details()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

def run_server():
    host = 'localhost'  # Change to your desired hostname or IP address
    port = 8000  # Change to your desired port

    server = HTTPServer((host, port), RequestHandler)
    print(f"Server started on {host}:{port}")
    server.serve_forever()

if __name__ == '__main__':
    run_server()

