import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row("О нас", "Выбор города")
    markup.row("Связаться с нами")

    markup2 = telebot.types.InlineKeyboardMarkup(row_width=2)
    item = telebot.types.InlineKeyboardButton("Москва", callback_data="Москва")
    item2 = telebot.types.InlineKeyboardButton("Казань", callback_data="Казань")
    item3 = telebot.types.InlineKeyboardButton("Омск", callback_data="Омск")
    item4 = telebot.types.InlineKeyboardButton("Иркутск", callback_data="Иркутск")
    markup2.add(item, item2, item3, item4)

    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name} {1.last_name}!\nЯ - бот <b>{2.first_name}</b>\nМы - компания. Официальный представитель государственных и частных Российских и Европейских ВУЗ-ов в средней Азии".format(message.from_user, message.from_user, bot.get_me()),
        parse_mode='html')
    bot.send_message(message.chat.id, "https://www.youtube.com/?v=SQWqa9tZYRM")
    bot.send_message(message.chat.id, "Для удобства есть меню, вы можете его скрыть нажав на соответствующую кнопку", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите город для поступления на учебу", reply_markup=markup2)

@bot.message_handler(content_types=['text'])
def lalala(message):
    markup2 = telebot.types.InlineKeyboardMarkup(row_width=2)
    item = telebot.types.InlineKeyboardButton("Москва", callback_data="Москва")
    item2 = telebot.types.InlineKeyboardButton("Казань", callback_data="Казань")
    item3 = telebot.types.InlineKeyboardButton("Омск", callback_data="Омск")
    item4 = telebot.types.InlineKeyboardButton("Иркутск", callback_data="Иркутск")
    markup2.add(item, item2, item3, item4)

    if message.text == "Выбор города":
        bot.send_message(message.chat.id, "Выберите город для поступленя на учебу", reply_markup=markup2)
    elif message.text == "О нас":
        bot.send_message(message.chat.id, "Официальный представитель государственных и частных Российских и Европейских ВУЗ-ов в средней Азии".format(message.from_user, message.from_user, bot.get_me()),
        parse_mode='html')
        bot.send_message(message.chat.id, "https://www.youtube.com/?v=SQWqa9tZYRM")
    elif message.text == "Связаться с нами":
        bot.send_message(message.chat.id, "Напишите нашему оепратору @taukee")

    else:
        bot.send_message(message.chat.id, "Я вас не понимаю")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    markup2 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup3 = telebot.types.InlineKeyboardMarkup(row_width=2)
    item = telebot.types.InlineKeyboardButton("Москва", callback_data="Москва")
    item2 = telebot.types.InlineKeyboardButton("Казань", callback_data="Казань")
    item3 = telebot.types.InlineKeyboardButton("Омск", callback_data="Омск")
    item4 = telebot.types.InlineKeyboardButton("Иркутск", callback_data="Иркутск")

    it1 = telebot.types.InlineKeyboardButton("МосАП", callback_data="МосАП")
    it2 = telebot.types.InlineKeyboardButton("Реавиз", callback_data="Реавиз")
    it3 = telebot.types.InlineKeyboardButton("ММА", callback_data="ММА")

    markup2.add(item, item2, item3, item4)
    markup3.add(it1,it2,it3)

    if call.message:
        if call.data == "Москва":
            bot.send_message(call.message.chat.id, "Вы выбрали Москву")
        elif call.data == "Казань":
            bot.send_message(call.message.chat.id, "Вы выбрали Казань")
        elif call.data == "Омск":
            bot.send_message(call.message.chat.id, "Вы выбрали Омск")
        elif call.data == "Иркутск":
            bot.send_message(call.message.chat.id, "Вы выбрали Иркутск")

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling(none_stop=True)