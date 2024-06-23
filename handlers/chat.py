import asyncio
from keyboard.main import main_keyboard
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from config import session
from data.base import GoToChat
from sqlalchemy import select
from keyboard.open_account import open_account_markup

router = Router()


@router.message(F.text == "👉 Переход в чат")
async def open_chat(message: types.Message):
    data_from_db = session.scalar(select(GoToChat))
    message_from_db = data_from_db.message
    reference_from_db = data_from_db.reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db if reference_from_db else ''}",
                         reply_markup=main_keyboard())
