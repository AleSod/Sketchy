import http.server
import socketserver
import webbrowser


webbrowser.open('http://localhost:48135/web/index.html', new=2)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 48135), handler) as httpd:
    httpd.serve_forever()