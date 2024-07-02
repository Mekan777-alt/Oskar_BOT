from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def back_rq_markup():
    buttons = [
        [KeyboardButton(text="👉 Отменить")],
    ]

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
