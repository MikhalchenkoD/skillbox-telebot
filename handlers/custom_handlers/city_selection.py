from loader import bot
from states.states import BotState
from utils.requests_to_api import get_location
from keyboards.inline.get_city_list_keyboard import gen_city_list_keyboard


@bot.message_handler(state=BotState.choosing_city)
def select_city(message):
    response = get_location(message.text)
    bot.send_message(message.chat.id, 'Выберите город', reply_markup=gen_city_list_keyboard(response['data']))