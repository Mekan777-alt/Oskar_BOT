from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cart_kazahstan():
    buttons = [
        [KeyboardButton(text="👉 Инструкция по открытию есть ИИН/НЕТ ИИН")],
        [KeyboardButton(text="👉 Инструкция по получению ИИН")],
        [KeyboardButton(text="👉 Ссылка на получение документов для налоговой и разъяснения")],
        [KeyboardButton(text="👉 В главное меню")],
    ]

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    return markup
