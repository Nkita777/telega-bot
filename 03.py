import telebot
from random import randint



bot = telebot.TeleBot("1459788300:AAHaJRpu3nstSTalXlYVkl3LedvNRzuYYvo")


words = ["антарктида","пылесос","акваланг"]
word = words[0]
print(word)

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я загадал слово! Попробуй его отгадать")


@bot.message_handler(content_types = ['text'])
def otvet(message):


    letter = message.text.lower()

    if len(letter) == 1:
        if letter in word:
            bot.send_message(message.chat.id, "Такая буква есть")

        else:
            bot.send_message(message.chat.id, "Такой буквы нет")
    else:
        if letter == word:
            bot.send_message(message.chat.id, "Вау ты угадал")
        else:
            bot.send_message(message.chat.id, "KAPPA OUTDATED  POGCHAMP OVERRATED  LONG HAVE WE WAITED  NOW YOU JEBAITED")
        
        
bot.polling()

