from telebot import types
from modules.lang_handler import _


def handle_game_selection(call, bot, game=None):
    game = game or call.data  # Используем переданное значение или значение из call.data
    photo_path = f'img/{game}.jpg'
    caption_text = _(f'{game}.intro')

    markup = types.InlineKeyboardMarkup()
    btn_registration = types.InlineKeyboardButton(_("menu.registration"), callback_data="registration")
    btn_rules = types.InlineKeyboardButton(_("menu.instruction"), callback_data=f"rules_{game}")
    btn_back = types.InlineKeyboardButton(_("menu.back"), callback_data=f"exit_{game}")
    markup.add(btn_registration, btn_rules, btn_back)

    try:
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=caption_text, reply_markup=markup)
    except FileNotFoundError:
        bot.send_message(call.message.chat.id, _('menu.error_image_not_found'))  # Сообщение об ошибке


def handle_registration(call, bot, url):
    registration_text = _('menu.registration_text')
    markup = types.InlineKeyboardMarkup()
    btn_register = types.InlineKeyboardButton(_('menu.register'), url=url)
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data="back_registration")
    markup.add(btn_register, btn_back)
    bot.send_message(call.message.chat.id, registration_text, reply_markup=markup)


def handle_back_registration(call, bot):
    handle_game_selection(call, bot)


def handle_rules(call, bot):
    game = call.data
    instruction_text = _('menu.instruction_text')
    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton(_('menu.back'), callback_data=f"exit_{game}")
    markup.add(btn_back)
    instruction_photo_path = 'img/inst.jpg'
    with open(instruction_photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo, caption=instruction_text, reply_markup=markup)


def handle_back_rules(call, bot):
    game = call.data.replace("exit_", "")  # Убираем префикс "exit_"
    handle_game_selection(call, bot, game)