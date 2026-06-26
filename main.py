import os
from kivy.app import App
from kivy.clock import Clock
from jnius import autoclass, cast

# Native Android Imports
PythonActivity = autoclass('org.kivy.android.PythonActivity')
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')

class WebWrapperApp(App):
    def build(self):
        # We return None as the UI is natively injected via WebView
        return None

    def on_start(self):
        # Schedule the native view injection on the main Android thread
        Clock.schedule_once(self.create_webview, 0)

    def create_webview(self, *args):
        activity = PythonActivity.mActivity
        
        # Initialize WebView
        webview = WebView(activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        
        # Prevent opening external browser
        webview.setWebViewClient(WebViewClient())

        # Resolve local file path
        # In Android/Kivy, assets are unpacked into the app folder
        current_dir = os.path.dirname(__file__)
        index_file = os.path.join(current_dir, 'web', 'index.html')
        
        # Load local HTML
        webview.loadUrl(f"file://{index_file}")

        # Map to Activity View
        activity.setContentView(webview, LayoutParams(
            LayoutParams.MATCH_PARENT, 
            LayoutParams.MATCH_PARENT
        ))

if __name__ == '__main__':
    WebWrapperApp().run()
