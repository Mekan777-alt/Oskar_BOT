from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def open_account_markup():
    buttons = [
        [KeyboardButton(text="👉 АМ")],
        [KeyboardButton(text="👉 ЮАР")],
        [KeyboardButton(text="👉 Казахстан")],
        [KeyboardButton(text="👉 В главное меню")],
    ]

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
