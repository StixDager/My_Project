import telebot
from config import TOKEN, CURRENCIES
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = (
        "👋 Привет! Я бот-конвертер валют.\n"
        "Чтобы узнать цену валюты, отправь сообщение в формате:\n"
        "<имя валюты> <в какую валюту перевести> <количество>\n\n"
        "Пример:\n"
        "`доллар рубль 100`\n\n"
        "Посмотреть доступные валюты: /values"
    )
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['values'])
def send_values(message):
    text = "📌 Доступные валюты:\n"
    for key in CURRENCIES:
        text += f"▫️ {key}\n"
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.split()

        if len(values) != 3:
            raise APIException("❗ Введите команду в формате: <валюта_из> <валюта_в> <количество>")

        base, quote, amount = values
        total = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Ошибка сервера:\n{e}")
    else:
        text = f"💱 {amount} {base} = {total:.2f} {quote}"
        bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)