#token 7513438563:AAFu4m2zL0fQhSg8QWQASwPVUxBZ53BYosk

import telebot
from telebot import types
from mines import handle_mines_selection, handle_registration, handle_back_registration, handle_rules_mines, handle_back_rules, handle_back_mines, handle_exit_selection
from tropicana import handle_tropicana_selection, handle_registration_tropicana, handle_back_registration_tropicana, handle_rules_tropicana, handle_back_rules_tropicana, handle_back_tropicana

# Ссылка для регистрации
url = "https://1wloom.top/casino/play/1play_1play_mines/?sub_1=486319246&open=register"

# Ваш токен
token = "7513438563:AAFu4m2zL0fQhSg8QWQASwPVUxBZ53BYosk"
bot = telebot.TeleBot(token)

# Приветственное сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем сообщение с выбором языка
    markup = types.InlineKeyboardMarkup()
    btn_russian = types.InlineKeyboardButton("Русский язык", callback_data="russian")
    markup.row(btn_russian)
    btn_english = types.InlineKeyboardButton("Английский язык", callback_data="english")
    markup.row(btn_english)
    
    bot.send_message(message.chat.id, "На каком языке продолжать?", reply_markup=markup)

# Удаление предыдущего сообщения перед отправкой нового
def delete_previous_message(call, bot):
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Обработка выбора языка
@bot.callback_query_handler(func=lambda call: call.data in ["russian", "english"])
def handle_language_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение

    if call.data == "russian":
        # Отправляем баннер с изображением и кнопками
        photo_path = 'img/photo.jpg'  # Замените на путь к вашей картинке
        caption_text = "Выберите игру:"

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Mines", callback_data="mines")
        btn2 = types.InlineKeyboardButton("Tropicana", callback_data="tropicana")
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton("Crash", callback_data="crash")
        btn4 = types.InlineKeyboardButton("Lucky Jet", callback_data="lucky_jet")
        markup.row(btn3, btn4)

        # Отправка изображения с текстом и кнопками
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=caption_text, reply_markup=markup)
    elif call.data == "english":
        bot.send_message(call.message.chat.id, "You have selected English.")
        # Здесь можно добавить дальнейшую логику для английского языка

# Обработка выбора игры mines
@bot.callback_query_handler(func=lambda call: call.data == "mines")
def mines_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_mines_selection(call, bot)  # Передаем объект bot

# Обработка выбора игры tropicana
@bot.callback_query_handler(func=lambda call: call.data == "tropicana")
def tropicana_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_tropicana_selection(call, bot)  # Передаем объект bot

# Обработка выбора регистрации
@bot.callback_query_handler(func=lambda call: call.data == "registration")
def registration_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_registration(call, bot, url)

# Обработка выбора регистрации tropicana
@bot.callback_query_handler(func=lambda call: call.data == "registration_tropicana")
def registration_selection_tropicana(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_registration_tropicana(call, bot, url)

# Обработка кнопки "Назад" на экране регистрации
@bot.callback_query_handler(func=lambda call: call.data == "back_registration")
def back_registration_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_registration(call, bot)

# Обработка кнопки "Назад" на экране регистрации
@bot.callback_query_handler(func=lambda call: call.data == "back_registration_tropicana")
def back_registration_selection_tropicana(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_registration_tropicana(call, bot)

# Обработка выбора инструкции
@bot.callback_query_handler(func=lambda call: call.data == "rules_mines")
def rules_mines_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_rules_mines(call, bot)

# Обработка выбора инструкции
@bot.callback_query_handler(func=lambda call: call.data == "rules_tropicana")
def rules_tropicana_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_rules_tropicana(call, bot)

# Обработка кнопки "Назад" на экране инструкции
@bot.callback_query_handler(func=lambda call: call.data == "exit_mines")
def back_rules_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_rules(call, bot)

# Обработка кнопки "Назад" на экране инструкции
@bot.callback_query_handler(func=lambda call: call.data == "exit_tropicana")
def back_rules_selection_tropicana(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_rules_tropicana(call, bot)

# Обработка кнопки "Выдать сигнал"
@bot.callback_query_handler(func=lambda call: call.data == "back_mines")
def back_mines_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_mines(call, bot)

# Обработка кнопки "Выдать сигнал"
@bot.callback_query_handler(func=lambda call: call.data == "back_tropicana")
def back_tropicana_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    handle_back_tropicana(call, bot)

# Обработка кнопки "Выбор языка"
@bot.callback_query_handler(func=lambda call: call.data == "start")
def handle_start_selection(call):
    delete_previous_message(call, bot)  # Удаляем предыдущее сообщение
    send_welcome(call.message)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Меня еще не научили этому")

if __name__ == '__main__':
    # Запускаем бота
    bot.polling()
