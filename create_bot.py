from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

try:
    bot = Bot(token=os.getenv('TOKEN'))
except:
    bot = Bot(token='5459494185:AAGuzC4SrqdA88aJWfXl0tAjd4Y7RuakIs4')

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
