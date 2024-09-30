import telebot
from telebot import types
from resources import token, url
from modules.lang_handler import _, set_language
from modules.game_handler import handle_game_selection, handle_game_rules, handle_game_registration, handle_game_signal

bot = telebot.TeleBot(token)
def start_bot():
    bot.polling()

def delete_previous_message(call, bot):
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_russian = types.InlineKeyboardButton("Русский язык", callback_data="russian")
    btn_english = types.InlineKeyboardButton("English language", callback_data="english")
    markup.row(btn_russian, btn_english)
    bot.send_message(message.chat.id, _('welcome.choose_language'), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["russian", "english"])
def handle_language_selection(call):
    delete_previous_message(call, bot)
    lang = 'ru' if call.data == "russian" else 'en'
    set_language(lang)
    show_game_selection(call.message)

def show_game_selection(message):
    photo_path = 'img/photo.jpg'
    caption_text = _('welcome.game_shoice')
    markup = types.InlineKeyboardMarkup()
    games = ["Mines", "Tropicana", "Crash", "Lucky Jet"]
    for i in range(0, len(games), 2):
        row = [types.InlineKeyboardButton(game, callback_data=game.lower().replace(" ", "_")) for game in games[i:i+2]]
        markup.row(*row)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=caption_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["mines", "tropicana", "crash", "lucky_jet"])
def game_selection(call):
    delete_previous_message(call, bot)
    handle_game_selection(call, bot, call.data)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rules_"))
def rules_selection(call):
    delete_previous_message(call, bot)
    game_name = call.data.split("_")[1]
    handle_game_rules(call, bot, game_name)

@bot.callback_query_handler(func=lambda call: call.data.startswith("registration_"))
def registration_selection(call):
    delete_previous_message(call, bot)
    game_name = call.data.split("_")[1]
    handle_game_registration(call, bot, url, game_name)

@bot.callback_query_handler(func=lambda call: call.data.startswith("back_in_game_"))
def registration_selection(call):
    delete_previous_message(call, bot)
    game_name = call.data.split("_")[-1]
    handle_game_selection(call, bot, game_name)

@bot.callback_query_handler(func=lambda call: call.data.startswith("signal_"))
def signal_selection(call):
    delete_previous_message(call, bot)
    game_name = call.data.split("_")[1]
    handle_game_signal(call, bot, game_name)

@bot.callback_query_handler(func=lambda call: call.data == "main_menu")
def handle_start_selection(call):
    delete_previous_message(call, bot)
    show_game_selection(call.message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, _('menu.error_message'))
    show_game_selection(message)