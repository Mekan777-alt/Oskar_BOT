import asyncio
from keyboard.main import main_keyboard
from keyboard.open_account import open_account_markup
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.depozite import markup_depozite

router = Router()


@router.message(F.text == "👉 Депозит")
async def get_depozite(message: types.Message):
    await message.answer("Тут будет описание раздела", reply_markup=markup_depozite())


@router.message(F.text == "👉 Cчет открыт")
async def check_depozite(message: types.Message):
    await message.answer("Тут отправляется инструкция")


@router.message(F.text == "👉 Cчет не открыт")
async def not_check_depozite(message: types.Message):
    await message.answer("Тут будет какое-то описание", reply_markup=open_account_markup())


@router.message(F.text == "👉 В главное меню")
async def get_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
