import os
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from kivy.app import App
from kivy.uix.webview import WebView

def run_local_server():
    # Target our assets directory
    os.chdir(os.path.join(os.path.dirname(__file__), 'www'))
    server_address = ("", 8080)
    with TCPServer(server_address, SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

class DragonApp(App):
    def build(self):
        # Start the background server thread
        threading.Thread(target=run_local_server, daemon=True).start()
        
        # Open and load full screen HTML design layout
        return WebView(url="http://127.0.0.1:8080/index.html")

if __name__ == '__main__':
    DragonApp().run()
  
