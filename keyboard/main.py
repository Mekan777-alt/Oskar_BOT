from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard():
    buttons = [
        [KeyboardButton(text="👉 Карта Казахстана")],
        [KeyboardButton(text="👉 Депозит")],
        [KeyboardButton(text="👉 Открытие счетов")],
        [KeyboardButton(text="👉 Переход в чат")],
        [KeyboardButton(text="👉 Перестановка USDT")],
        [KeyboardButton(text="👉 FAQ заводы/выводы")],
        [KeyboardButton(text="👉 Обратная связь")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons)

    return markup
