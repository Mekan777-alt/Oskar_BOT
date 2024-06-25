from keyboard.main import main_keyboard
from aiogram import Router, F, types
from config import session
from sqlalchemy import select


router = Router()


@router.message(F.text == "👉 Переход в чат")
async def open_chat(message: types.Message):
    data_from_db = session.scalar(select(GoToChat))
    message_from_db = data_from_db.message
    reference_from_db = data_from_db.reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db if reference_from_db else ''}",
                         reply_markup=main_keyboard())
