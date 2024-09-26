#token 7513438563:AAFu4m2zL0fQhSg8QWQASwPVUxBZ53BYosk

import telebot
from telebot import types
from mines import handle_mines_selection, handle_registration, handle_back_registration, handle_rules_mines, handle_back_rules, handle_back_mines, handle_exit_selection


# Ваш токен
token = "7513438563:AAFu4m2zL0fQhSg8QWQASwPVUxBZ53BYosk"
bot = telebot.TeleBot(token)

# Приветственное сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем сообщение с выбором языка
    markup = types.InlineKeyboardMarkup()
    btn_russian = types.InlineKeyboardButton("Русский язык", callback_data="russian")
    btn_english = types.InlineKeyboardButton("Английский язык", callback_data="english")
    markup.row(btn_russian, btn_english)
    
    bot.send_message(message.chat.id, "На каком языке продолжать?", reply_markup=markup)

# Обработка выбора языка
@bot.callback_query_handler(func=lambda call: call.data in ["russian", "english"])
def handle_language_selection(call):
    if call.data == "russian":
        # Отправляем баннер с изображением и кнопками
        photo_path = 'img/photo.jpg'  # Замените на путь к вашей картинке
        caption_text = "Выберите игру:"

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Mines", callback_data="mines")
        btn2 = types.InlineKeyboardButton("Tropicana", callback_data="tropicana")
        btn3 = types.InlineKeyboardButton("Crash", callback_data="crash")
        btn4 = types.InlineKeyboardButton("Lucky Jet", callback_data="lucky_jet")
        markup.row(btn1, btn2, btn3, btn4)

        # Отправка изображения с текстом и кнопками
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=caption_text, reply_markup=markup)
    elif call.data == "english":
        bot.send_message(call.message.chat.id, "You have selected English.")
        # Здесь можно добавить дальнейшую логику для английского языка

# Обработка выбора игры mines
@bot.callback_query_handler(func=lambda call: call.data == "mines")
def mines_selection(call):
    handle_mines_selection(call, bot)  # Передаем объект bot

# Обработка выбора регистрации
@bot.callback_query_handler(func=lambda call: call.data == "registration")
def registration_selection(call):
    handle_registration(call, bot)

# Обработка кнопки "Назад" на экране регистрации
@bot.callback_query_handler(func=lambda call: call.data == "back_registration")
def back_registration_selection(call):
    handle_back_registration(call, bot)

# Обработка выбора инструкции
@bot.callback_query_handler(func=lambda call: call.data == "rules_mines")
def rules_mines_selection(call):
    handle_rules_mines(call, bot)

# Обработка кнопки "Назад" на экране инструкции
@bot.callback_query_handler(func=lambda call: call.data == "exit_mines")
def back_rules_selection(call):
    handle_back_rules(call, bot)

# Обработка кнопки "Выдать сигнал"
@bot.callback_query_handler(func=lambda call: call.data == "back_mines")
def back_mines_selection(call):
    handle_back_mines(call, bot)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Меня еще не научили этому")

if __name__ == '__main__':
    # Запускаем бота
    bot.polling()
