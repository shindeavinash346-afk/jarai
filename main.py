import os
import speech_recognition as sr
import pyttsx3

# Text to Speech Engine Setup
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
        engine.say(text)
            engine.runAndWait()

            # Voice Input Logic
            def listen():
                r = sr.Recognizer()
                    with sr.Microphone() as source:
                            print("Listening...")
                                    r.pause_threshold = 1
                                            audio = r.listen(source)
                                                try:
                                                        query = r.recognize_google(audio, language='en-US')
                                                                print(f"You: {query}")
                                                                        return query.lower()
                                                                            except Exception:
                                                                                    return ""

                                                                                    if __name__ == "__main__":
                                                                                        speak("Systems online, Boss. How can I assist you today?")
                                                                                            while True:
                                                                                                    command = listen()
                                                                                                            if "sleep" in command or "exit" in command:
                                                                                                                        speak("Going offline, Boss.")
                                                                                                                                    break
                                                                                                                                            elif command != "":
                                                                                                                                                        speak(f"Processing your request: {command}")⁹