from gtts import gTTS
import os

my_text = str(input("Enter your text: "))
language = "ko"
# language = "en"
my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj.save("result1.mp3")
os.system("result1.mp3")
