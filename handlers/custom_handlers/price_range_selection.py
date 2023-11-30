from loader import bot
from states.states import BotState
from utils.requests_to_api import get_house
from keyboards.inline.get_list_house_keyboard import gen_list_house_keyboard


@bot.message_handler(state=BotState.choosing_price_range)
def select_price_range(message):
    price_range = message.text.split('-')
    data_for_request = {}

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data_for_request['min_price'] = price_range[0]
        data_for_request['max_price'] = price_range[1]
        data_for_request['method'] = data['method']
        data_for_request['city'] = data['city']

    bot.delete_state(message.from_user.id, message.chat.id)
    response = get_house(data_for_request)

    if not response['data']:
        bot.send_message(message.chat.id, 'Доступных домов не найдено')
    else:
        bot.send_message(message.chat.id, 'Доступные дома', reply_markup=gen_list_house_keyboard(response['data']))
