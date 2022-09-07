import telebot
from telebot import types

bot = telebot.TeleBot('5782277261:AAEmSgX62TVRT7pitAhS-Dy8-U9ONIH-6HU')

# commands
@bot.message_handler(commands=['start'])
def command_start(message):
    mess = f'Здравствуйте, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def command_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт DNS", url='https://www.dns-shop.ru/'))
    markup.add(types.InlineKeyboardButton("Посетить сайт MVideo", url='https://www.mvideo.ru/'))
    bot.send_message(message.chat.id, "Рекоменуемые сайты:", reply_markup=markup)


@bot.message_handler(commands=['help'])
def command_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_start = types.KeyboardButton('Старт')
    btn_websiteDNS = types.KeyboardButton('Рекомендуемые сайты')

    markup.add(btn_start, btn_websiteDNS)
    bot.send_message(message.chat.id, "Список команд ниже", reply_markup=markup)


# content types
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет" or message.text == "Здравствуйте":
        bot.send_message(message.chat.id, "Что я могу сделать для Вас?", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('./images/friends.jpg', 'rb')
        bot.send_photo(message.chat.id, photo) 
    elif message.text == "Старт":
        command_start(message)
    elif message.text == "Рекомендуемые сайты":
        command_website(message)
    else:
        bot.send_message(message.chat.id, "Не понятен Ваш запрос", parse_mode='html')
        # bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Зачетное фото!", parse_mode='html')


bot.polling(non_stop=True)