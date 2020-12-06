import telebot
from random import randint



bot = telebot.TeleBot("1459788300:AAHaJRpu3nstSTalXlYVkl3LedvNRzuYYvo")

animals = ["тигр", "леопард"]
geography = ["австралия", "африка"]
space = ["скафандр", "луна"]
other = ["антарктида","пылесос","акваланг"]

word = None
letters = []




@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text ="Животные", callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text="География", callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text="Космос", callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text="Разное", callback_data=4))
    bot.send_message(message.chat.id, text="Привет, я загадал слово! Выбери тему и попробуй его отгадать:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_hamdler(call):

    if call.data == "1":
        words = animals

    elif call.data == "2":
        words = geography

    elif call.data == "3":
        words = space

    elif call.data == "4":
        words = other

    global word
    word = words[randint(0, len(words)-1)]

    #letters = ["___" for x in range(len(word))]



    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "Я загадал слово, в нем "+str(len(word)) + " букв. Попробуй его отгадать!")



@bot.message_handler(content_types = ['text'])
def otvet(message):
    print(word, " word")
    letter = message.text.lower()
    print(letter)

    if len(letter) == 1:
        if letter in word:
            bot.send_message(message.chat.id, "Такая буква есть")
            letters.append(letter)

        else:
            bot.send_message(message.chat.id, "Такой буквы нет")
    else:
        if letter == word:
            bot.send_message(message.chat.id, "Вау ты угадал")
        else:
            bot.send_message(message.chat.id, "KAPPA OUTDATED  POGCHAMP OVERRATED  LONG HAVE WE WAITED  NOW YOU JEBAITED")

    prompt =''
    for l in word:
        if l in letters:
            prompt+=l
        else:
            prompt+="___"

    bot.send_message(message.chat.id, prompt)
bot.polling()
