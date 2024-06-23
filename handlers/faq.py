import asyncio
from keyboard.main import main_keyboard
from aiogram import Router, F, types


router = Router()


@router.message(F.text == "👉 FAQ заводы/выводы")
async def open_chat(message: types.Message):
    await message.answer("Тут будет какая-то логика", reply_markup=main_keyboard())