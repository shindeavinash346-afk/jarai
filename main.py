import json
import ssl
import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

RAW_KEY = "AQ.Ab8RN6J-I3dqbPRph9n-YQSMw765DdhyHycmr7ZrguYPpXaPGg"

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JarvisUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.status_label = Label(
            text="J.A.R.V.I.S. ONLINE\nAsk me anything, Boss.",
            font_size='18sp',
            halign='center',
            valign='middle',
            size_hint=(1, 0.5)
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.add_widget(self.status_label)

        self.user_input = TextInput(
            hint_text="Type command or question here...",
            multiline=False,
            size_hint=(1, 0.2),
            font_size='16sp'
        )
        self.add_widget(self.user_input)

        self.ask_btn = Button(
            text="ASK JARVIS",
            font_size='18sp',
            size_hint=(1, 0.2),
            background_color=(0, 0.6, 1, 1)
        )
        self.ask_btn.bind(on_press=self.process_ai_request)
        self.add_widget(self.ask_btn)

    def process_ai_request(self, instance):
        query = self.user_input.text.strip()
        if not query:
            self.status_label.text = "JARVIS: Please enter a command first, Boss."
            return

        self.status_label.text = "JARVIS: Thinking..."
        Clock.schedule_once(lambda dt: self.get_gemini_response(query), 0.1)

    def get_gemini_response(self, query):
        try:
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={RAW_KEY}"
            prompt_text = f"You are JARVIS, an advanced AI assistant. Keep responses brief (1-2 sentences max) and address the user as Boss. Query: {query}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt_text}]
                }]
            }
            data = json.dumps(payload).encode('utf-8')
            
            headers = {
                'Content-Type': 'application/json',
                'x-goog-api-key': RAW_KEY
            }
            
            req = urllib.request.Request(url, data=data, headers=headers)
            context = ssl._create_unverified_context()
            
            with urllib.request.urlopen(req, timeout=15, context=context) as response:
                result = json.loads(response.read().decode('utf-8'))
                reply = result['candidates'][0]['content']['parts'][0]['text']
                self.status_label.text = f"JARVIS: {reply}"
                self.user_input.text = ""
        except Exception as e:
            self.status_label.text = f"JARVIS Error: {str(e)}"

class JarvisApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JarvisApp().run()
        self.ask_btn = Button(
            text="ASK JARVIS",
            font_size='18sp',
            size_hint=(1, 0.2),
            background_color=(0, 0.6, 1, 1)
        )
        self.ask_btn.bind(on_press=self.process_ai_request)
        self.add_widget(self.ask_btn)

    def process_ai_request(self, instance):
        query = self.user_input.text.strip()
        if not query:
            self.status_label.text = "JARVIS: Please enter a command first, Boss."
            return

        self.status_label.text = "JARVIS: Thinking..."
        Clock.schedule_once(lambda dt: self.get_gemini_response(query), 0.1)

    def get_gemini_response(self, query):
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={RAW_KEY}"
            prompt_text = f"You are JARVIS, an advanced AI assistant. Keep responses brief (1-2 sentences max) and address the user as Boss. Query: {query}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt_text}]
                }]
            }
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(
                url, 
                data=data, 
                headers={'Content-Type': 'application/json'}
            )
            
            # Bypass SSL certificate verification for Android
            context = ssl._create_unverified_context()
            
            with urllib.request.urlopen(req, timeout=10, context=context) as response:
                result = json.loads(response.read().decode('utf-8'))
                reply = result['candidates'][0]['content']['parts'][0]['text']
                self.status_label.text = f"JARVIS: {reply}"
                self.user_input.text = ""
        except Exception as e:
            self.status_label.text = f"JARVIS Error: {str(e)}"

class JarvisApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JarvisApp().run()
