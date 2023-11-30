from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_city_list_keyboard(city_list):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    for item in city_list:
        if item['areaType'] == 'city':
            markup.add(InlineKeyboardButton(f"Город: {item['city']} | Штат: {item['state']}", callback_data=f"city#{item['key']}"))

    return markup
