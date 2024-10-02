from telebot import types
from modules.registration import is_user_registered, register_user
from modules.lang_handler import _

from resources import url


def handle_game_selection(call, bot, game_name):
    photo_path = f'img/{game_name}.jpg'
    caption_text = _(f'{game_name}.{game_name}_caption')

    markup = types.InlineKeyboardMarkup()
    btn_registration = types.InlineKeyboardButton(_("menu.registration"), callback_data=f"registration_{game_name}")
    btn_instruction = types.InlineKeyboardButton(_("menu.instruction"), callback_data=f"rules_{game_name}")
    markup.row(btn_registration, btn_instruction)
    btn_signal = types.InlineKeyboardButton(_("menu.issue_a_signal"), callback_data=f"signal_{game_name}")
    btn_language = types.InlineKeyboardButton(_("menu.back"), callback_data="main_menu")
    markup.row(btn_signal, btn_language)

    with open(photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=caption_text, reply_markup=markup)


def handle_game_rules(call, bot, game_name):
    instruction_text = _(f'menu.instruction_text')
    instruction_photo_path = f'img/inst.jpg'

    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data=f"back-in-game_{game_name}")
    markup.row(btn_back)

    with open(instruction_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=instruction_text, reply_markup=markup)


def handle_game_registration(call, bot, url, game_name):
    register_user(call.from_user.id)
    registration_text = _('menu.registration_text')

    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton(_('menu.register'), url=url)
    markup.row(btn_register)
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data=f"back-in-game_{game_name}")
    markup.row(btn_back)

    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)


def handle_game_signal(call, bot, game_name):
    user_id = call.from_user.id
    if is_user_registered(user_id):
        markup = types.InlineKeyboardMarkup()
        webapp_button = types.InlineKeyboardButton(_("menu.get_a_signal"), web_app=types.WebAppInfo(f'https://ikaragodin.ru/gampling-tg/{game_name}app/index.html'))
        markup.add(webapp_button)
        bot.send_message(call.message.chat.id, _('menu.you_are_registered'), reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, _('menu.error_register'))
        handle_game_registration(call, bot, url, game_name)