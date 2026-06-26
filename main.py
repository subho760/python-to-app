import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.logger import Logger

# Import Android specific components only when running on target OS
if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')

class WebAppContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(WebAppContainer, self).__init__(**kwargs)
        if platform == 'android':
            self.setup_android_webview()
        else:
            Logger.info("WebView: Standard Desktop Mode initialized.")

    def setup_android_webview(self):
        # Fetch current system activity reference
        activity = PythonActivity.mActivity
        
        # Create WebView instance running contextually on the main thread
        self.webview = WebView(activity)
        self.settings = self.webview.getSettings()
        
        # Enable full web functionality features
        self.settings.setJavaScriptEnabled(True)
        self.settings.setDomStorageEnabled(True)
        self.settings.setAllowFileAccess(True)
        self.settings.setAllowContentAccess(True)
        self.settings.setDatabaseEnabled(True)
        
        # Ensure links open inside the app instead of an external browser
        self.webview.setWebViewClient(WebViewClient())
        
        # Bind the WebView container size natively to fill parent layout
        activity.runOnUiThread(self.create_webview_layout)

    def create_webview_layout(self):
        activity = PythonActivity.mActivity
        layout_params = LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
        
        # Resolve path target to the root index.html located in the packed www folder
        base_path = os.path.join(os.path.dirname(__file__), 'www', 'index.html')
        target_url = f"file://{base_path}"
        
        Logger.info(f"WebView: Attempting to render target -> {target_url}")
        self.webview.loadUrl(target_url)
        
        # Add layout directly to activity view stack
        activity.addContentView(self.webview, layout_params)

class DragonHoleApp(App):
    def build(self):
        return WebAppContainer()

if __name__ == '__main__':
    DragonHoleApp().run()
