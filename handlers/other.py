from aiogram import types
from aiogram import Dispatcher
from create_bot import dp


import json
import string


# @dp.message_handler()
async def hello(message: types.Message):
    if message.text.lower() in ('привет', 'ку', 'здарова', 'салам', 'че как'):
        await message.reply('И тебе привет!')
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('Запрет.json')))) != set():
        await message.reply('Мат запрещен!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(hello)
