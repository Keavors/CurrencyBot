import telebot
from config import keys, TOKEN
from utils import ConvertionException, Converter

bot = telebot.TeleBot(TOKEN)


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
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConvertionException('Слишком много параметров.')
        elif len(values) < 3:
            raise ConvertionException('Слишком мало параметров.')

        quote, base, amount = values
        total_base, amount = Converter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:
        text = f'Цена {amount} {quote} в {base} - {amount * total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
