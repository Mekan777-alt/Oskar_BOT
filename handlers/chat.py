from keyboard.main import main_keyboard
from aiogram import Router, F, types
from config import bot
from db.repository.go_to_chat import get_message, get_reference, message_for_go_to_chat


router = Router()


@router.message(F.text == "👉 Переход в чат")
async def open_chat(message: types.Message):
    message_text = message_for_go_to_chat()
    await message.answer(text=message_text, reply_markup=main_keyboard())
