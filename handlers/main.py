from aiogram import Router, types
from aiogram.filters.command import Command
from keyboard.main import main_keyboard


router = Router()


@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Тут сообщение приветствия", reply_markup=main_keyboard())
