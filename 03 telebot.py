import telebot

bot = telebot.TeleBot("1459788300:AAHaJRpu3nstSTalXlYVkl3LedvNRzuYYvo")


last_message = "Привет"









@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ну приветик, очень рад видеть у себя в гостях,чувствуй себя как дома")




#define-объявить





@bot.message_handler(commands = ['photo'])
def send_picture(message):
    with open("LOL.jpg", 'rb') as cat:
        bot.send_photo(message.chat.id, cat)





@bot.message_handler(content_types = ['text'])
def otvet (message):
    global last_message
    bot.send_message(message.chat.id, message.from_user.first_name + ", "+ last_message)
    last_message = message.text


bot.polling()








