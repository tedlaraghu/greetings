from greets import greetings
from translate import Translator
import yagmail
import pandas

translator = Translator(to_lang='te')

yagmail.SMTP(user="tedla.harika@gmail.com", password="Abbhilash")

text = pandas.read_csv('people.csv')


for greeting in greetings:
    print(translator.translate(greeting).title() + " :) :) :)")
