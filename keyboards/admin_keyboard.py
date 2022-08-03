from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove


cens_on = KeyboardButton('/cens_on')
cens_off = KeyboardButton('/cens_off')

kb_cens = ReplyKeyboardMarkup(resize_keyboard=True)

kb_cens.row(cens_on, cens_off)
