from telebot import types
from registration import is_user_registered, register_user

# Словарь для отслеживания статуса регистрации пользователей
#user_registered = {}

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
    markup.row(btn_action1, btn_action2)
    btn_action3 = types.InlineKeyboardButton("Выдать сигнал", callback_data="back_mines")
    btn_action4 = types.InlineKeyboardButton("Выбор языка", callback_data="start")
    markup.row(btn_action3, btn_action4)

    # Отправка изображения с текстом и кнопками
    with open(mines_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=mines_caption, reply_markup=markup)

# Обработка выбора инструкции
def handle_rules_mines(call, bot):  # Добавляем новую функцию
    # Отправляем текст инструкции и картинку
    instruction_text = (
        "Бот основан и обучен на кластере нейросети от OpenAI  🖥 [ChatGPT-v4.2.0]\n"
        "Для тренировки бота было сыграно приблизительно 13 000 игр.\n"
        "В данный момент пользователи бота успешно делают в день 20-30% от своего депозита!\n"
        "В данный момент бот всё ещё обучается и точность бота составляет 85%!\n"
        "Для получения максимального профита следуйте следующей инструкции:\n"
        "👉🏻 1. Пройти регистрацию в букмекерской конторе 1WIN.\n"
        "Если не открывается - заходим с включенным VPN (Швеция).\n"
        "Без регистрации доступ к сигналам не будет открыт!\n"
        "👉🏻 2. Пополнить баланс своего аккаунта.\n"
        "👉🏻 3. Перейти в раздел 1WIN Games и выбрать игру 💣 'mines'.\n"
        "👉🏻 4. Запросить сигнал в боте и ставить по сигналам из бота.\n"
        "👉🏻 5. При неудачном сигнале советуем удвоить ставку, что бы полностью перекрыть потерю при следующем сигнале.\n"
    )
    
    instruction_photo_path = 'img/mines-inst.jpg'  # Замените на путь к картинке для инструкции

    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton("Назад", callback_data="exit_mines")
    markup.row(btn_back)

    # Отправляем изображение с текстом и кнопкой назад
    with open(instruction_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=instruction_text, reply_markup=markup)

# Обработка выбора регистрации
def handle_registration(call, bot, url):  # Добавляем параметр bot
    # Обновляем статус пользователя как зарегистрированного
    register_user[call.from_user.id] = True  # Ставим False до проверки

    # Отправляем текст с кнопками "Зарегистрироваться" и "Назад"
    registration_text = (
        "Для корректной связи с нейросетью, требуется зарегистрироваться по нашей ссылке. "
        "Нейросеть синхронизируется с вашим аккаунтом для расчета личных сигналов."
    )
    
    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton("Зарегистрироваться", url=url)  # Замените на вашу ссылку
    markup.row(btn_register)
    btn_back = types.InlineKeyboardButton("Назад", callback_data="back_registration")
    markup.row(btn_back)

    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)


# Обработка кнопки "Выдать сигнал"
def handle_back_mines(call, bot):
    user_id = call.from_user.id
    if user_id in register_user and register_user[user_id]:  # Если пользователь зарегистрирован
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
        handle_registration(call, bot)

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
