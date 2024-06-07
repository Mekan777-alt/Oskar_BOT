from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def markup_depozite():
    buttons = [
        [KeyboardButton(text="👉 Cчет открыт")],
        [KeyboardButton(text="👉 Cчет не открыт")],
        [KeyboardButton(text="👉 В главное меню")],
    ]

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
