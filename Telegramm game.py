import telebot
from random import randint



bot = telebot.TeleBot("1459788300:AAHaJRpu3nstSTalXlYVkl3LedvNRzuYYvo")


random_number = 0
counter = 0

@bot.message_handler(commands = ['start'])
def start_message(message):
    global random_number
    bot.send_message(message.chat.id, "Ну приветик, очень рад видеть у себя в гостях,чувствуй себя как дома")
    random_number = randint(0, 100)


@bot.message_handler(commands = ['tell'])
def tell_number(message):
    bot.send_message(message.chat.id, str(random_number))
    random_number = randint(0, 100)


#define "def" -объявить



@bot.message_handler(content_types = ['text'])
def otvet (message):
    global counter
    
    try:
        user_number = int(message.text)#превращаем ответ пользователя из строки(str)число(int)
       
        counter += 1
        
        if user_number == random_number:
            bot.send_message(message.chat.id, str(counter) + "  PERFECT! You guessed")
            
        elif user_number > random_number:
            bot.send_message(message.chat.id, "Too big")

        elif user_number < random_number:
            bot.send_message(message.chat.id, "Too small")
        
        else:
            bot.send_message(message.chat.id, str(random_number) + "я загадал это число")
            
    except:
        bot.send_message(message.chat.id, "WRONG!!! ONLY NUMBERS")



bot.polling()

