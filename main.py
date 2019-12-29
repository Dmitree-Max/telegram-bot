import telebot
import random

bot = telebot.TeleBot('token')
random.seed()

stickers = ["CAADAgADPQADHwFMFfy3DuyWLxQIFgQ", "CAADAgADTAADHwFMFRXJNftorSX-FgQ", "CAADAgADUgADHwFMFceIFqRTvZ8eFgQ",
            "CAADAgADRAADHwFMFfwY2ouYYa4YFgQ", "CAADAgADZAADHwFMFUzefHz0bzbpFgQ", "CAADAgADQwADHwFMFTvw6tJiToNqFgQ",
            "CAADAgADSgADHwFMFez-0iBiCIPGFgQ", "CAADAgADYAADHwFMFX-M1iKFpz-MFgQ", "CAADAgADUAADHwFMFXAQI5_3oM6tFgQ"]


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.add('Magic')
    msg = bot.reply_to(message, 'Want some magic?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)


def process_step(message):
    chat_id = message.chat.id
    if message.text == 'Magic':
        bot.send_sticker(chat_id, stickers[random.randint(0, 6)])
    else:
        bot.send_message(chat_id, 'Please, push Magic button')


@bot.message_handler(content_types=['text'])
def send_text(message):
    chat_id = message.chat.id
    if message.text == 'Magic':
        bot.send_sticker(chat_id, stickers[random.randint(0, 8)])
    else:
        bot.send_message(chat_id, 'Please, push Magic button')



bot.polling()


