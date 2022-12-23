import telebot
from config import keys, TOKEN
from extensions import APIException, Exchange


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду в следующем формате:' \
           '\nИмя валюты' \
           '\nВ какую валюту перевести' \
           '\nКоличество переводимой валюты' \
            '\nЧтобы увидеть все доступные валюты: /values '
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Слишком много параметров')

        quote, base, amount = values
        total_base = Exchange.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Некорректные данные \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
