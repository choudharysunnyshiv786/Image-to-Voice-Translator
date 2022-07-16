import pytesseract
from googletrans import Translator
from gtts import gTTS
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = Image.open('img2.png')
rs = pytesseract.image_to_string(img)

line = rs.replace('\n', ' ')
print("Text in image given is --->"+line)

language = input("Enter the language of voice: ")

LANGUAGES = {
'afrikaans': 'af',
'arabic': 'ar',
'bulgarian': 'bg',
'bengali': 'bn',
'bosnian': 'bs',
'catalan': 'ca',
'czech': 'cs',
'welsh': 'cy',
'danish': 'da',
'german': 'de',
'greek': 'el',
'english': 'en',
'esperanto': 'eo',
'spanish': 'es',
'estonian': 'et',
'finnish': 'fi',
'french': 'fr',
'gujarati': 'gu',
'hindi': 'hi',
'croatian': 'hr',
'hungarian': 'hu',
'armenian': 'hy',
'indonesian': 'id',
'icelandic': 'is',
'italian': 'it',
'japanese': 'ja',
'javanese': 'jw',
'khmer': 'km',
'kannada': 'kn',
'korean': 'ko',
'latin': 'la',
'latvian': 'lv',
'macedonian': 'mk',
'malayalam': 'ml',
'marathi': 'mr',
'myanmar': 'my',
'nepali': 'ne',
'dutch': 'nl',
'norwegian': 'no',
'polish': 'pl',
'portuguese': 'pt',
'romanian': 'ro',
'russian': 'ru',
'sinhala': 'si',
'slovak': 'sk',
'albanian': 'sq',
'serbian': 'sr',
'sundanese': 'su',
'swedish': 'sv',
'swahili': 'sw',
'tamil': 'ta',
'telugu': 'te',
'thai': 'th',
'filipino': 'tl',
'turkish': 'tr',
'ukrainian': 'uk',
'urdu': 'ur',
'vietnamese': 'vi',
'chinese': 'zh-CN',
'chinese(Mandarin/Taiwan)': 'zh-TW',
}

if language not in LANGUAGES:
    print(language)
    print("Translation in this language is not available!")
    exit()

trans = Translator()
out = trans.translate(line, dest=LANGUAGES[language])
print("Translated text is --->"+out.text)

myAudioObj = gTTS(text=out.text, lang=LANGUAGES[language], slow=False)
myAudioObj.save("final.mp3")
os.startfile('final.mp3')
