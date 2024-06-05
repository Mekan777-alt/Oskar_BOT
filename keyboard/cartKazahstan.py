from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cart_kazahstan():
    buttons = [
        [KeyboardButton(text="👉 Инструкция по открытию есть ИИН/НЕТ ИИН")]
    ]

    markup = ReplyKeyboardMarkup(keyboard=buttons)

    return markup
