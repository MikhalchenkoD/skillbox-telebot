from loader import bot
from states.states import BotState
from utils.requests_to_api import get_house
from keyboards.inline.get_list_house_keyboard import gen_list_house_keyboard


@bot.message_handler(commands=["high", 'low', 'custom'])
def set_selection_state(message):
    bot.set_state(message.from_user.id, BotState.choosing_city, message.chat.id)
    bot.send_message(message.chat.id, 'Напиши в каком городе ты хочешь дом')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['method'] = message.text.split()[0][1:]