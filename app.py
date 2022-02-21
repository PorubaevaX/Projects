import telebot

from config import *
from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду в следующем формате:\n<название валюты для конвертации> \
<в какую валюту перевести> \
<количество переводимой валюты>\n\nПосмотреть список всех доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base, sym, amount = message.text.split()
    except ValueError as e:
        bot.reply_to(message, "Неверное количество параметров!")
    try:
        new_price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f'Цена {amount} {base} в {sym} : {new_price}')
    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')

bot.polling()
