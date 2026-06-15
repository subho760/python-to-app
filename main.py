import os
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread

class ReusableHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True

def run_local_server(www_path):
    # Subclass handler to serve from a specific directory without global os.chdir()
    class FixedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=www_path, **kwargs)

    server_address = ('127.0.0.1', 8080)
    try:
        with ReusableHTTPServer(server_address, FixedHandler) as httpd:
            httpd.serve_forever()
    except Exception as e:
        print(f"Local server error: {e}")

class NativeWebContainer(Widget):
    def __init__(self, **kwargs):
        super(NativeWebContainer, self).__init__(**kwargs)
        # Schedule webview creation on the next frame
        Clock.schedule_once(self.create_native_webview, 0)

    @run_on_ui_thread
    def create_native_webview(self, *args):
        # Resolve classes within the UI thread for stability
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity

        webview = WebView(activity)
        settings = webview.getSettings()
        
        # Performance and compatibility settings
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setUseWideViewPort(True)
        settings.setLoadWithOverviewMode(True)
        settings.setAllowFileAccess(True)
        
        # Set a standard client to handle navigation within the app
        webview.setWebViewClient(WebViewClient())
        activity.setContentView(webview)

        # Fix Race Condition: Wait briefly for the server thread to bind the port
        def deferred_load(dt):
            webview.loadUrl('http://127.0.0.1:8080/index.html')
        Clock.schedule_once(deferred_load, 0.5)

class DragonApp(App):
    def build(self):
        # Safely resolve absolute path to the 'www' directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        www_path = os.path.join(base_dir, 'www')
        
        # Start server with path argument instead of global chdir
        server_thread = threading.Thread(
            target=run_local_server, 
            args=(www_path,), 
            daemon=True
        )
        server_thread.start()
        
        return NativeWebContainer()

if __name__ == '__main__':
    DragonApp().run()
