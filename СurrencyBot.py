import telebot


TOKEN = '7209060346:AAGWbVLkT8t03m-hPQlYx9ri9YraI22oobU'

bot = telebot.TeleBot(TOKEN)

keys = {'биткоин': 'BTC', 'эфириум': 'ETH', 'доллар': 'USD'}


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

bot.polling()