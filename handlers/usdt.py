from keyboard.main import main_keyboard
from aiogram import Router, F, types
from config import session
from sqlalchemy import select
from data.base import USDT

router = Router()


@router.message(F.text == "👉 Перестановка USDT")
async def open_chat(message: types.Message):
    data_from_db = session.scalar(select(USDT))
    message_from_db = data_from_db.message
    reference_from_db = data_from_db.reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db}",
                         reply_markup=main_keyboard())
