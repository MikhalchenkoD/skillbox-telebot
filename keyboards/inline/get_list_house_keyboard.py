from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_list_house_keyboard(house_list):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    for item in house_list:
        if item['price']:
            markup.add(InlineKeyboardButton(f"Адрес: {item['location']['address']} | Цена: {item['price']}", url=item['url']))

    return markup
