from keyboard.main import main_keyboard
from keyboard.open_account import open_account_markup
from aiogram import Router, F, types
from config import bot
from keyboard.depozite import markup_depozite
from db.repository.deposited import get_document, get_document_reserved, message_for_deposited


router = Router()


@router.message(F.text == "👉 Депозит")
async def get_depozite(message: types.Message):
    await message.answer("Тут будет описание раздела", reply_markup=markup_depozite())


@router.message(F.text == "👉 Cчет открыт")
async def check_depozite(message: types.Message):
    message_text = message_for_deposited()
    await message.answer(text=message_text, reply_markup=main_keyboard())
    if get_document():
        await bot.send_document(chat_id=message.from_user.id, document=get_document())
    if get_document_reserved():
        await bot.send_document(chat_id=message.from_user.id, document=get_document_reserved())


@router.message(F.text == "👉 Cчет не открыт")
async def not_check_depozite(message: types.Message):
    await message.answer("Тут будет какое-то описание", reply_markup=open_account_markup())


@router.message(F.text == "👉 В главное меню")
async def get_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
