import asyncio
from keyboard.main import main_keyboard
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.open_account import open_account_markup

router = Router()


@router.message(F.text == "👉 Открытие счетов")
async def open_account(message: types.Message):
    await message.answer("Тут описание раздела", reply_markup=open_account_markup())


@router.message(F.text == "👉 АМ")
async def get_AM(message: types.Message):
    await message.answer("Тут будет описание - инструкция по открытию - инструкция по пополнению")


@router.message(F.text == "👉 ЮАР")
async def get_UAR(message: types.Message):
    await message.answer("Тут будет описание - инструкция по открытию - инструкция по пополнению")


@router.message(F.text == "👉 Казахстан")
async def get_kz(message: types.Message):
    await message.answer("Тут будет описание - инструкция по открытию - инструкция по пополнению")


@router.message(F.text == "👉 В главное меню")
async def back_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
    