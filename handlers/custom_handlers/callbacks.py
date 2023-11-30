from loader import bot
from states.states import BotState
from utils.requests_to_api import get_house
from keyboards.inline.get_list_house_keyboard import gen_list_house_keyboard

@bot.callback_query_handler(func=lambda call: call.data in ['low', 'high', 'custom'])
def set_city_selection_state(call):
    bot.set_state(call.from_user.id, BotState.choosing_city, call.message.chat.id)
    bot.send_message(call.message.chat.id, 'Напиши в каком городе ты хочешь дом')
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['method'] = call.data


@bot.callback_query_handler(func=lambda call: 'city#' in call.data)
def save_city(call):
    data_for_request = {}

    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['city'] = call.data.split('#')[1]
        data_for_request['method'] = data['method']
        data_for_request['city'] = data['city']

    if data_for_request['method'] != 'custom':
        bot.delete_state(call.from_user.id, call.message.chat.id)
        response = get_house(data_for_request)

        if not response['data']:
            bot.send_message(call.message.chat.id, 'Доступных домов не найдено')
        else:
            bot.send_message(call.message.chat.id, 'Доступные дома',
                             reply_markup=gen_list_house_keyboard(response['data']))
    else:
        bot.set_state(call.from_user.id, BotState.choosing_price_range, call.message.chat.id)
        bot.send_message(call.message.chat.id, 'Введите диапазон цен. Например: 1000-20000')
