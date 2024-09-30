from telebot import types

from modules.registration import is_user_registered, register_user
from resources import url
from modules.lang_handler import _

def handle_mines_selection(call, bot):  # Добавляем параметр bot
    # Отправляем изображение, текст и кнопки для Mines
    mines_photo_path = 'img/mines.jpg'
    mines_caption = _('mines.mines_caption')

    markup = types.InlineKeyboardMarkup()
    btn_action1 = types.InlineKeyboardButton(_("menu.registration"), callback_data="registration")
    btn_action2 = types.InlineKeyboardButton(_("menu.instruction"), callback_data="rules_mines")
    markup.row(btn_action1, btn_action2)
    btn_action3 = types.InlineKeyboardButton(_("menu.issue_a_signal"), callback_data="back_mines")
    btn_action4 = types.InlineKeyboardButton(_("menu.choice_of_language"), callback_data="start")
    markup.row(btn_action3, btn_action4)

    # Отправка изображения с текстом и кнопками
    with open(mines_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=mines_caption, reply_markup=markup)

# Обработка выбора инструкции
def handle_rules_mines(call, bot):  # Добавляем новую функцию
    # Отправляем текст инструкции и картинку
    instruction_text = _('menu.instruction_text')
    
    instruction_photo_path = 'img/inst.jpg'  # Замените на путь к картинке для инструкции

    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data="exit_mines")
    markup.row(btn_back)

    # Отправляем изображение с текстом и кнопкой назад
    with open(instruction_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=instruction_text, reply_markup=markup)

# Обработка выбора регистрации
def handle_registration(call, bot, url):  # Добавляем параметр bot
    # Обновляем статус пользователя как зарегистрированного
    register_user(call.from_user.id)

    # Отправляем текст с кнопками "Зарегистрироваться" и "Назад"
    registration_text = _('menu.registration_text')
    
    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton(_('menu.register'), url=url)  # Замените на вашу ссылку
    markup.row(btn_register)
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data="back_registration")
    markup.row(btn_back)

    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)


# Обработка кнопки "Выдать сигнал"
def handle_back_mines(call, bot):
    user_id = call.from_user.id
    if is_user_registered(user_id):  # Если пользователь зарегистрирован
        # Создаем WebApp-кнопку
        markup = types.InlineKeyboardMarkup()
        webapp_url = "https://ikaragodin.ru/gampling-tg/minesapp/index.html"  # Замените на ссылку на ваш WebApp
        webapp_button = types.InlineKeyboardButton(_("menu.get_a_signal"), web_app=types.WebAppInfo(webapp_url))
        markup.add(webapp_button)
        
        # Отправляем пользователю кнопку для открытия WebApp
        bot.send_message(call.message.chat.id, _('menu.you_are_registered'), reply_markup=markup)
    else:
        # Если пользователь не зарегистрировался, отправляем напоминание о регистрации
        bot.send_message(call.message.chat.id, _('menu.error_register'))
        handle_registration(call, bot, url)

# Обработка кнопки "Назад" на экране регистрации
def handle_back_registration(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору игры
    handle_mines_selection(call, bot)  # Передаем объект bot

# Обработка кнопки "Назад" на экране инструкции
def handle_back_rules(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору игры
    handle_mines_selection(call, bot)  # Передаем объект bot

# Обработка кнопки "Выбор языка"
def handle_exit_selection(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору языка
    send_welcome(call.message)

# Дополнительно — можно реализовать проверку перехода по ссылке регистрации (например, через API или анализ переходов на сторонних платформах).
