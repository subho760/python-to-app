import os
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

# Create a custom threaded server that allows immediate port reuse
class ReusableHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True

def run_local_server():
    # Safely resolve the absolute path to the unpacked www directory on Android
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(base_dir, 'www'))
    
    server_address = ('127.0.0.1', 8080)
    
    # Using our custom server prevents the Errno 98 port crashes
    with ReusableHTTPServer(server_address, SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

class NativeWebContainer(Widget):
    def __init__(self, **kwargs):
        super(NativeWebContainer, self).__init__(**kwargs)
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
        
        # Enable debugging (Allows you to use chrome://inspect/#devices on your PC)
        WebView.setWebContentsDebuggingEnabled(True)

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
    
