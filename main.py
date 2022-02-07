from greets import greetings
from translate import Translator

translator = Translator(to_lang='te')


for greeting in greetings:
    print(translator.translate(greeting).title() + " :) :) :)")
