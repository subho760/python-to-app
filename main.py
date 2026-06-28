import os
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class DragonHoleApp(App):
    def build(self):
        # Create a clean vertical layout
        self.layout = BoxLayout(orientation='vertical')
        
        # This will hold and display your background images
        self.bg_image = Image()
        self.layout.add_widget(self.bg_image)
        
        # Interactive Control Button
        btn = Button(
            text="Tap to change background image",
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.change_to_random_image)
        self.layout.add_widget(btn)
        
        return self.layout

    def change_to_random_image(self, instance):
        folder_path = "images"
        
        # Check if the folder exists in your project directory
        if os.path.exists(folder_path):
            # Scan the folder dynamically for any image filenames
            all_images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            if all_images:
                # Grab an image filename completely at random
                random_choice = random.choice(all_images)
                
                # Combine it to find the asset path (e.g., "images/my_photo.jpg")
                full_image_path = os.path.join(folder_path, random_choice)
                
                # Update the display layout smoothly
                self.bg_image.source = full_image_path
                self.bg_image.reload()
            else:
                instance.text = "Error: No images found in folder!"
        else:
            instance.text = "Error: 'images' folder missing!"

if __name__ == '__main__':
    DragonHoleApp().run()
