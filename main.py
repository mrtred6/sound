from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import os

class SoundApp(App):
    def build(self):
        sound_path = os.path.join(os.path.dirname(__file__), "assets", "Child.wav")  # مسیر فایل صوتی در پوشه assets
        self.sound = SoundLoader.load(sound_path)
        self.image = Image(source="")  # تصویر اولیه خالی است
        layout = BoxLayout(orientation='vertical')
        
        play_button = Button(text="play", on_press=self.play_sound)
        stop_button = Button(text="stop", on_press=self.stop_sound)
        show_image_button = Button(text="aks", on_press=self.show_image)
        
        layout.add_widget(play_button)
        layout.add_widget(stop_button)
        layout.add_widget(show_image_button)
        layout.add_widget(self.image)
        
        return layout
    
    def play_sound(self, instance):
        if self.sound:
            self.sound.play()
    
    def stop_sound(self, instance):
        if self.sound:
            self.sound.stop()
    
    def show_image(self, instance):
        image_path = os.path.join(os.path.dirname(__file__), "assets", "image.png")  # مسیر تصویر در پوشه assets
        self.image.source = image_path
        self.image.reload()

if __name__ == "__main__":
    SoundApp().run()
