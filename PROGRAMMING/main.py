import telebot
import config
from googletrans import Translator



bot = telebot.TeleBot(config.tg_token)

translator = Translator(service_urls=['translate.googleapis.com'])


@bot.message_handler(commands=['vocabulary'])
def show_vocabulary(message):
     with open("vocabulary.txt", "r") as file:
          lines = file.readlines()[-10:]
     for line in reversed(lines):
          bot.send_message(message.chat.id, text=line)

@bot.message_handler(content_types=['text'])
def handle_message(message):
     #bot.send_message(message.chat.id, text="Hi, Buddy!")
     bot.send_message(message.chat.id, text=translator.translate(message.text, src="en", dest="ru").text)
     with open("vocabulary.txt", "a") as file:
          file.write(message.text + "\n")


bot.polling()

