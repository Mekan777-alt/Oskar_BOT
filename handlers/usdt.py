from keyboard.main import main_keyboard
from aiogram import Router, F, types
from db.repository.usdt import message_for_usdt

router = Router()


@router.message(F.text == "👉 Перестановка USDT")
async def open_chat(message: types.Message):
    message_text = message_for_usdt()
    if message_text:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
