import os
from keyboard.main import main_keyboard
from aiogram import Router, F, types
from keyboard.open_account import open_account_markup
from config import bot, session
from sqlalchemy import select
from data.base import OpenAccount

router = Router()


@router.message(F.text == "👉 Открытие счетов")
async def open_account(message: types.Message):
    await message.answer("Тут описание раздела", reply_markup=open_account_markup())


@router.message(F.text == "👉 АМ")
async def get_AM(message: types.Message):
    data_from_db = session.scalar(select(OpenAccount))
    message_from_db = data_from_db.item3_1_message
    reference_from_db = data_from_db.item3_1_reference
    # doc1 = open(f"{os.getcwd()}/files/FRHC_FFA_Savings Accounts_ru (2).pdf", "rb")
    # doc2 = open(f"{os.getcwd()}/files/Открытие счета Армения.pdf", "rb")
    await message.answer(f"{message_from_db}\n\n{reference_from_db}")

    # await bot.send_document(document=doc1, chat_id=message.from_user.id)
    # await bot.send_document(document=doc2, chat_id=message.from_user.id)


@router.message(F.text == "👉 Казахстан")
async def get_kz(message: types.Message):
    data_from_db = session.scalar(select(OpenAccount))
    message_from_db = data_from_db.item3_2_message
    reference_from_db = data_from_db.item3_2_reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db}")


@router.message(F.text == "👉 В главное меню")
async def back_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
    