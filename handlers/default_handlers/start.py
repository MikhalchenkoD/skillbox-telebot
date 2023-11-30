from telebot.types import Message
from keyboards.inline.get_start_keyboard import gen_start_keyboard
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, 'Привет, я бот риелтор, готов помочь тебе в поиске дома твоей мечты', reply_markup=gen_start_keyboard())
