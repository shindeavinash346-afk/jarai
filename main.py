import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JarvisUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Title Label
        self.status_label = Label(
            text="J.A.R.V.I.S. ONLINE\nTap Speak to talk",
            font_size='22sp',
            halign='center'
        )
        self.add_widget(self.status_label)

        # Speak Button
        self.speak_btn = Button(
            text="LISTEN / SPEAK",
            font_size='20sp',
            size_hint=(1, 0.3),
            background_color=(0, 0.7, 1, 1)
        )
        self.speak_btn.bind(on_press=self.start_listening)
        self.add_widget(self.speak_btn)

    def start_listening(self, instance):
        self.status_label.text = "Listening..."
        # Simulated response test
        Clock.schedule_once(self.respond, 2)

    def respond(self, dt):
        self.status_label.text = "JARVIS: Systems are 100% operational, Boss."

class JarvisApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JarvisApp().run()
