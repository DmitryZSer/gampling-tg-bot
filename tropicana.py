from telebot import types
from registration import is_user_registered, register_user

# Словарь для отслеживания статуса регистрации пользователей
#user_registered = {}

def handle_tropicana_selection(call, bot):  # Добавляем параметр bot
    # Отправляем изображение, текст и кнопки для Mines
    tropicana_photo_path = 'img/mines.jpg'  # Замените на путь к картинке для Mines
    tropicana_caption = (
        "Добро пожаловать в 🌊 игру TROPICANA 🏄‍♀️"
        "🏄‍♀️ Tropicana - это игра, в которой вы делаете ставку на увеличивающийся множитель до того, как девушка едет на доске для серфинга. Чем дольше вы ждете, тем выше ваш потенциальный выигрыш, но если девушка уедет до того, как вы получите деньги, вы проиграете."
        "Наш бот поможет найти оптимальное время для вашей ставке."
    )

    markup = types.InlineKeyboardMarkup()
    btn_action1 = types.InlineKeyboardButton("Регистрация", callback_data="registration_tropicana")
    btn_action2 = types.InlineKeyboardButton("Инструкция", callback_data="rules_tropicana")
    markup.row(btn_action1, btn_action2)
    btn_action3 = types.InlineKeyboardButton("Выдать сигнал", callback_data="back_tropicana")
    btn_action4 = types.InlineKeyboardButton("Выбор языка", callback_data="start")
    markup.row(btn_action3, btn_action4)

    # Отправка изображения с текстом и кнопками
    with open(tropicana_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=tropicana_caption, reply_markup=markup)

# Обработка выбора инструкции
def handle_rules_tropicana(call, bot):  # Добавляем новую функцию
    # Отправляем текст инструкции и картинку
    instruction_text = (
        "инструкция для тропикана"
    )
    
    instruction_photo_path = 'img/mines-inst.jpg'  # Замените на путь к картинке для инструкции

    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton("Назад", callback_data="exit_tropicana")
    markup.row(btn_back)

    # Отправляем изображение с текстом и кнопкой назад
    with open(instruction_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=instruction_text, reply_markup=markup)

# Обработка выбора регистрации
def handle_registration_tropicana(call, bot, url):  # Добавляем параметр bot
    # Обновляем статус пользователя как зарегистрированного
    register_user(call.from_user.id)
    # Отправляем текст с кнопками "Зарегистрироваться" и "Назад"
    registration_text = (
        "Для корректной связи с нейросетью, требуется зарегистрироваться по нашей ссылке. "
        "Нейросеть синхронизируется с вашим аккаунтом для расчета личных сигналов."
    )
    
    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton("Зарегистрироваться", url=url)  # Замените на вашу ссылку
    markup.row(btn_register)
    btn_back = types.InlineKeyboardButton("Назад", callback_data="back_registration_tropicana")
    markup.row(btn_back)

    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)


# Обработка кнопки "Выдать сигнал"
def handle_back_tropicana(call, bot):
    #user_id = call.from_user.id
    if is_user_registered(call.from_user.id):  # Если пользователь зарегистрирован
        # Создаем WebApp-кнопку
        markup = types.InlineKeyboardMarkup()
        webapp_url = "https://ikaragodin.ru/gampling-tg/minesapp/index.html"  # Замените на ссылку на ваш WebApp
        webapp_button = types.InlineKeyboardButton("Получить сигнал", web_app=types.WebAppInfo(webapp_url))
        markup.add(webapp_button)
        
        # Отправляем пользователю кнопку для открытия WebApp
        bot.send_message(call.message.chat.id, "Вы зарегистрированы!", reply_markup=markup)
    else:
        # Если пользователь не зарегистрировался, отправляем напоминание о регистрации
        bot.send_message(call.message.chat.id, "Чтобы получить сигнал, необходимо зарегистрироваться.")
        handle_registration_tropicana(call, bot)

# Обработка кнопки "Назад" на экране регистрации
def handle_back_registration_tropicana(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору игры
    handle_tropicana_selection(call, bot)  # Передаем объект bot

# Обработка кнопки "Назад" на экране инструкции
def handle_back_rules_tropicana(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору игры
    handle_tropicana_selection(call, bot)  # Передаем объект bot

# Обработка кнопки "Выбор языка"
def handle_exit_selection(call, bot):  # Добавляем параметр bot
    # Возвращаем пользователя к выбору языка
    send_welcome(call.message)

# Дополнительно — можно реализовать проверку перехода по ссылке регистрации (например, через API или анализ переходов на сторонних платформах).
