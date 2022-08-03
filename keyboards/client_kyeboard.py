from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove


button_1 = KeyboardButton('/work_time')
button_2 = KeyboardButton('/menu')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить геолокацию', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_1).add(button_2).row(b4, b5)
