from greets import greetings
from translate import Translator
import yagmail

translator = Translator(to_lang='te')

yagmail.SMTP(user="tedla.harika@gmail.com", password="Abbhilash")


for greeting in greetings:
    print(translator.translate(greeting).title() + " :) :) :)")
