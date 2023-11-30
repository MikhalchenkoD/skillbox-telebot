from telebot.handler_backends import State, StatesGroup

class BotState(StatesGroup):
    choosing_city = State()
    choosing_price_range = State()