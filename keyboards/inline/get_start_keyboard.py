from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_start_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Сначала дорогие дома", callback_data="high"),
        InlineKeyboardButton("Сначала дешевые дома", callback_data="low"),
        InlineKeyboardButton("Вывести дома по пользовательским настройкам", callback_data="custom"),
        InlineKeyboardButton("История", callback_data="history"),
    )

    return markup
