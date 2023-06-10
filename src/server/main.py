import http.server
import socketserver

# Define the port number to listen on
PORT = 8000

# Define the request handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

# Create a TCP/IP socket server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server listening on port {PORT}")
    httpd.serve_forever()