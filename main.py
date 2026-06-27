import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class DesignContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(DesignContainer, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 30

        # Create basic Canvas background layer
        with self.canvas.before:
            self.bg_color = Color(0.07, 0.07, 0.07, 1) # Dark charcoal (#121212 alternative)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Content Elements
        self.add_widget(Label(
            text="Dragon Hole", 
            font_size='32sp', 
            bold=True,
            size_hint_y=0.2
        ))
        
        self.add_widget(Label(
            text="Testing Status: Functional", 
            font_size='18sp',
            color=(0, 1, 0.53, 1), # Green indicator text color
            size_hint_y=0.2
        ))

        # Action Interactive Control
        self.btn = Button(
            text="Tap to Change Background",
            font_size='18sp',
            bold=True,
            background_normal='',
            background_color=(0, 1, 0.53, 1),
            color=(0.07, 0.07, 0.07, 1),
            size_hint_y=0.2,
            border=(20, 20, 20, 20)
        )
        self.btn.bind(on_press=self.rotate_background_color)
        self.add_widget(self.btn)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def rotate_background_color(self, instance):
        # Update Canvas RGB values safely on touch action events
        self.bg_color.rgb = (random.random(), random.random(), random.random())

class MainWrapperApp(App):
    def build(self):
        return DesignContainer()

if __name__ == '__main__':
    MainWrapperApp().run()
