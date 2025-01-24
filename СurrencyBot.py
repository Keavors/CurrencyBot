import json
import requests
import telebot

TOKEN = '7209060346:AAGWbVLkT8t03m-hPQlYx9ri9YraI22oobU'

bot = telebot.TeleBot(TOKEN)

keys = {'биткоин': 'BTC', 'эфириум': 'ETH', 'доллар': 'USD'}


class ConvertionException(Exception):
    pass


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать введите:\n<имя валюты> <в какую валюты перевести> <количество переводимой валюты>\n'
            'Увидеть список всех доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for k in keys:
        text = '\n'.join((text, k))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException('Невозможно конвертировать одинаковые валюты.')

    if quote not in keys:
        raise ConvertionException(f'Невозможно конвертировать валюту {quote}.')

    if base not in keys:
        raise ConvertionException(f'Невозможно конвертировать валюту {base}.')

    try:
        amount = int(amount)
    except:
        raise ConvertionException(f'Не удалось обработать количество {amount}.')

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {amount * total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
