import telebot
from random import randint



bot = telebot.TeleBot("1459788300:AAHaJRpu3nstSTalXlYVkl3LedvNRzuYYvo")


random_number = 0






@bot.message_handler(commands = ['start'])
def start_message(message):
    global random_number
    bot.send_message(message.chat.id, "Ну приветик, очень рад видеть у себя в гостях,чувствуй себя как дома")
    random_number = randint(0, 100)



#define-объявить







@bot.message_handler(content_types = ['text'])
def otvet (message):
    try:
        user_number = int(message.text)#превращаем ответ пользователя из строки(str)число(int)
        if user_number == random_number:
            bot.send_message(message.chat.id, "PERFECT! You guessed")
            
        elif user_number > random_number:
            bot.send_message(message.chat.id, "Too big")
        
        else:
            bot.send_message(message.chat.id, "Too small")
            
    except:
        bot.send_message(message.chat.id, "WRONG!!! ONLY NUMBERS")     



bot.polling()









