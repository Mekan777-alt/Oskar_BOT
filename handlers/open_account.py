from keyboard.main import main_keyboard
from aiogram import Router, F, types
from keyboard.open_account import open_account_markup
from config import bot
from db.repository.open_account3_1 import message_for_open_account3_1, get_document3_1, get_document_reserved3_1
from db.repository.open_account3_2 import message_for_open_account3_2, get_document3_2, get_document_reserved3_2


router = Router()


@router.message(F.text == "👉 Открытие счетов")
async def open_account(message: types.Message):
    await message.answer("Тут описание раздела", reply_markup=open_account_markup())


@router.message(F.text == "👉 АМ")
async def get_AM(message: types.Message):
    message_text = message_for_open_account3_1()
    if message_text:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    if get_document3_1():
        await bot.send_document(chat_id=message.from_user.id, document=get_document3_1())
    if get_document_reserved3_1():
        await bot.send_document(chat_id=message.from_user.id, document=get_document_reserved3_1())


@router.message(F.text == "👉 Казахстан")
async def get_kz(message: types.Message):
    message_text = message_for_open_account3_2()
    if message_text:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    if get_document3_2():
        await bot.send_document(chat_id=message.from_user.id, document=get_document3_2())
    if get_document_reserved3_2():
        await bot.send_document(chat_id=message.from_user.id, document=get_document_reserved3_2())


@router.message(F.text == "👉 В главное меню")
async def back_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
    