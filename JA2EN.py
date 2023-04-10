import speech_recognition as sr
from deep_translator import GoogleTranslator
import keyboard
import pyttsx3

keytopress = ';'
#押すキー変更

mic = sr.Recognizer()

def on_key_press(event):
    if event.name == keytopress:
        try:
            with sr.Microphone() as source:
                print(u"聞き取り中...")
                voice = mic.listen(source)
                txt = mic.recognize_google(voice, language="ja")  #話す言語変更
                
                result = GoogleTranslator(source='auto',target='en').translate(txt) #英語以外pyttsx3は受け付けないので触ってはいけない
                engine = pyttsx3.init()
                engine.setProperty("rate", 140)
                engine.say(result)
                engine.runAndWait()

                                
                print(result)

        except:
            print("もう一度、はっきりと大きな声でお願いします。")

keyboard.on_press(on_key_press)

keyboard.wait()
