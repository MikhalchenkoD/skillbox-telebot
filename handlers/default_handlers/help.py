from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from keyboards.inline.get_start_keyboard import gen_start_keyboard
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    bot.send_message(message.chat.id, 'Вот с чем я могу тебе помочь',
                     reply_markup=gen_start_keyboard())
