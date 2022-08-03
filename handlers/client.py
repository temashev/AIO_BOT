from aiogram import types
from aiogram import Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Привет! Имя бота - psychokid_deadinside_ghoul_kanekiken1000-7\n'
                                                     f'\nНапишите "/help" для получения полного списка команд',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(f'Общение с ботом через ЛС, напишите ему:\nhttps://t.me/idkwtbid_bot')


async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'\t\t<i><b>Вот полный список команд:</b></i>\n\n'
                                                 f'/start - <i>Начать общение с ботом</i>\n'
                                                 f'/help - <i>Полный список команд бота</i>\n'
                                                 f'/work_time <i>or</i> /Режим_работы - <i>Узнать время работы '
                                                 f'магазина</i>\n',
                           parse_mode='html')


# @dp.message_handler(commands=['Режим_работы'])
async def work_time(message: types.Message):
    await bot.send_message(message.from_user.id, f'Режим работы: <b>круглосуточно</b>', parse_mode='html')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(work_time, commands=['work_time', 'режим_работы'])
