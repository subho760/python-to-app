import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create a large interactive button
        self.btn = Button(
            text="Tap to Change Color!",
            font_size='24sp',
            background_normal='',
            background_color=get_color_from_hex('#34495e')
        )
        self.btn.bind(on_release=self.change_color)
        self.add_widget(self.btn)

    def change_color(self, instance):
        # Generate a random hex color
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        self.btn.background_color = get_color_from_hex(color)
        self.btn.text = f"Color: {color}"

class ModernApp(App):
    def build(self):
        # Set a default clear color for the window
        Window.clearcolor = (1, 1, 1, 1)
        return RootWidget()

if __name__ == "__main__":
    ModernApp().run()
