import asyncio
from keyboard.main import main_keyboard
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.open_account import open_account_markup

router = Router()


@router.message(F.text == "👉 Открытие счетов")
async def open_account(message: types.Message):
    await message.answer("Тут описание раздела", reply_markup=open_account_markup())
