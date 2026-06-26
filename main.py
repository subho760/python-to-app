import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')

class WebViewContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(WebViewContainer, self).__init__(**kwargs)
        if platform == 'android':
            self.setup_webview()

    def setup_webview(self):
        activity = PythonActivity.mActivity
        self.webview = WebView(activity)
        settings = self.webview.getSettings()
        
        # Configure full local web execution environments
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setAllowFileAccess(True)
        settings.setAllowContentAccess(True)
        
        self.webview.setWebViewClient(WebViewClient())
        activity.runOnUiThread(self.load_local_web)

    def load_local_web(self):
        activity = PythonActivity.mActivity
        params = LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
        
        # Target local web directory entry point
        html_path = os.path.join(os.path.dirname(__file__), 'web', 'index.html')
        self.webview.loadUrl(f"file://{html_path}")
        activity.addContentView(self.webview, params)

class MainWrapperApp(App):
    def build(self):
        return WebViewContainer()

if __name__ == '__main__':
    MainWrapperApp().run()
