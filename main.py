import os
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass

# Run the UI initialization inside the safe Android application UI thread pool
from android.runnable import run_on_ui_thread

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

def run_local_server():
    # Point directly to your assets folder
    os.chdir(os.path.join(os.path.dirname(__file__), 'www'))
    server_address = ("127.0.0.1", 8080)
    with TCPServer(server_address, SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

class NativeWebContainer(Widget):
    def __init__(self, **kwargs):
        super(NativeWebContainer, **kwargs)
        # Safely schedule the view layer creation once clock cycles start
        Clock.schedule_once(self.create_native_webview, 0)

    @run_on_ui_thread
    def create_native_webview(self, *args):
        webview = WebView(activity)
        settings = webview.getSettings()
        
        # Core settings to allow fluid high-performance HTML5 canvas configurations
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setUseWideViewPort(True)
        settings.setLoadWithOverviewMode(True)
        
        wvc = WebViewClient()
        webview.setWebViewClient(wvc)
        
        # Set the main android context to hold our canvas
        activity.setContentView(webview)
        webview.loadUrl('http://127.0.0.1:8080/index.html')

class DragonApp(App):
    def build(self):
        # Fire up the lightweight assets background server
        threading.Thread(target=run_local_server, daemon=True).start()
        return NativeWebContainer()

if __name__ == '__main__':
    DragonApp().run()
    
