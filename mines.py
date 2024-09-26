from telebot import types

# Словарь для отслеживания статуса регистрации пользователей
user_registered = {}

def handle_mines_selection(call, bot):  # Добавляем параметр bot
    # Отправляем изображение, текст и кнопки для Mines
    mines_photo_path = 'img/mines.jpg'  # Замените на путь к картинке для Mines
    mines_caption = (
        "Добро пожаловать в бот-сигнал игры 💣 MINES 💣\n"
        "Mines — это гэмблинг игра в букмекерской конторе 1WIN, которая основывается на классическом 'Сапёре'.\n"
        "Ваша цель — открывать безопасные ячейки и не попадаться в ловушки.\n\n"
        "Наш бот основан на нейросети от OpenAI!\n"
        "Он может предугадать расположение звёзд с вероятностью 85%."
    )

    markup = types.InlineKeyboardMarkup()
    btn_action1 = types.InlineKeyboardButton("Регистрация", callback_data="registration")
    btn_action2 = types.InlineKeyboardButton("Инструкция", callback_data="rules_mines")
    btn_action3 = types.InlineKeyboardButton("Выдать сигнал", callback_data="back_mines")
    btn_action4 = types.InlineKeyboardButton("Выбор языка", callback_data="exit_mines")
    markup.row(btn_action1, btn_action2, btn_action3, btn_action4)

    # Отправка изображения с текстом и кнопками
    with open(mines_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=mines_caption, reply_markup=markup)

# Обработка выбора регистрации
def handle_registration(call, bot):  # Добавляем параметр bot
    # Обновляем статус пользователя как зарегистрированного
    user_registered[call.from_user.id] = False  # Ставим False до проверки

    # Отправляем текст с кнопками "Зарегистрироваться" и "Назад"
    registration_text = (
        "Для корректной связи с нейросетью, требуется зарегистрироваться по нашей ссылке. "
        "Нейросеть синхронизируется с вашим аккаунтом для расчета личных сигналов."
    )
    
    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton("Зарегистрироваться", url="https://1wloom.top/casino/play/1play_1play_mines/?sub_1=486319246&open=register")  # Замените на вашу ссылку
    btn_back = types.InlineKeyboardButton("Назад", callback_data="back_registration")
    markup.row(btn_register, btn_back)

    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)

# Обработка кнопки "Выдать сигнал"
def handle_back_mines(call, bot):
    #user_id = call.from_user.id
    #if user_id in user_registered and user_registered[user_id]:  # Если пользователь зарегистрирован
        # Создаем WebApp-кнопку
        markup = types.InlineKeyboardMarkup()
        webapp_url = "http://192.168.254.104:5000"  # Замените на ссылку на ваш WebApp
        webapp_button = types.InlineKeyboardButton("Получить сигнал", web_app=types.WebAppInfo(webapp_url))
        markup.add(webapp_button)
        
        # Отправляем пользователю кнопку для открытия WebApp
        bot.send_message(call.message.chat.id, "Вы зарегистрированы! Откройте WebApp для получения сигнала.", reply_markup=markup)
    #else:
        # Если пользователь не зарегистрировался, отправляем напоминание о регистрации
    #    bot.send_message(call.message.chat.id, "Чтобы получить сигнал, необходимо зарегистрироваться.")
    #    handle_registration(call, bot)

# Обработка кнопки "Назад" на экране регистрации
def handle_back_registration(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору игры
    handle_mines_selection(call, bot)  # Передаем объект bot

# Обработка кнопки "Выбор языка"
def handle_exit_selection(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору языка
    from bot import send_welcome  # Импортируем send_welcome здесь, чтобы избежать циклического импорта
    send_welcome(call.message)

# Дополнительно — можно реализовать проверку перехода по ссылке регистрации (например, через API или анализ переходов на сторонних платформах).
