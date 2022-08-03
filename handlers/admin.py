from abc import ABC

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot


ID = None


class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    desciption = State()
    price = State()


# Getting an ID current moderator
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Вы прошли проверку!\nЧто нужно сделать?')
    await bot.send_message(message.chat.id, f'Пользователь {message.from_user.first_name} является админом')
    if message.from_user.id != ID:
        await bot.send_message(message.chat.id, f'Пользователь {message.from_user.first_name} не админ')
    await message.delete()


# Starts dialog a load a new step menu
# @dp.message_handler(commands=['Загрузить'], state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Загрузить фото')
    else:
        await bot.send_message('Ты не прошел проверку лох')


# Catching first answer and adding to dictionary
# @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply('Теперь название')


# Catching second answer
# @dp.message_handler(state=FSMadmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Описание')


# Catching 3d answer
# @dp.message_handler(state=FSMadmin.desciption)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMadmin.next()
        await message.reply('Теперь цена')


# Catching last 4th answer
# @dp.message_handler(state=FSMadmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        async with state.proxy() as data:
            await message.reply(str(data))

        await state.finish()


# Exit from FSM
# @dp.message_handler(state='*', commands=['отмена', 'exit'])
# @dp.message_handler(Text(equals=['отмена', 'exit'], ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply(f'<b>OK</b>\nРегистрация успешно отменена!', parse_mode='html')


# Register handlers
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)

    dp.register_message_handler(cm_start, commands=['Загрузить', 'load'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_description, state=FSMadmin.desciption)
    dp.register_message_handler(load_price, state=FSMadmin.price)

    dp.register_message_handler(cancel_handler, state='*', commands=['отмена', 'exit'])
    dp.register_message_handler(cancel_handler, Text(equals=['отмена', 'exit'], ignore_case=True), state='*')
