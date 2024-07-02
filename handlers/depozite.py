from keyboard.main import main_keyboard
from keyboard.open_account import open_account_markup
from aiogram import Router, F, types
from config import bot
from keyboard.depozite import markup_depozite
from db.repository.deposited import get_document, get_document_reserved, message_for_deposited
from .settings import delete_file, download_file
from aiogram.types import FSInputFile


router = Router()


@router.message(F.text == "👉 Депозит")
async def get_depozite(message: types.Message):
    await message.answer("Сейчас предлагаем депозит в долларах США с привлекательной процентной ставкой 8.8% "
                         "годовых.\nЭто отличная возможность для Вас увеличить свои сбережения с минимальными рисками",
                         reply_markup=markup_depozite())


@router.message(F.text == "👉 Cчет открыт")
async def check_depozite(message: types.Message):
    message_text = message_for_deposited()
    if len(message_text) > 2:
        await message.answer(text=message_text, reply_markup=main_keyboard())

    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    document_url = get_document()
    if document_url:
        await bot.send_chat_action(chat_id=message.from_user.id, action="upload_document")

        local_filename = str(document_url).split('/')[-1]
        try:
            file_down = await download_file(f"http://91.142.74.227:8000/media/{document_url}", local_filename)
            send_file = FSInputFile(file_down)
            await bot.send_document(chat_id=message.from_user.id, document=send_file)
        except Exception as e:
            await message.answer(text=f"Ошибка загрузки документа: {e}")
        finally:
            await delete_file(local_filename)

    document_reserved_url = get_document_reserved()
    if document_reserved_url:

        await bot.send_chat_action(chat_id=message.from_user.id, action="upload_document")

        local_filename = str(document_reserved_url).split('/')[-1]
        try:
            file_down = await download_file(f"http://91.142.74.227:8000/media/{document_reserved_url}", local_filename)
            send_file = FSInputFile(file_down)
            await bot.send_document(chat_id=message.from_user.id, document=send_file)
        except Exception as e:
            await message.answer(text=f"Ошибка загрузки документа: {e}")
        finally:
            await delete_file(local_filename)


@router.message(F.text == "👉 Cчет не открыт")
async def not_check_depozite(message: types.Message):
    await message.answer("Тут будет какое-то описание", reply_markup=open_account_markup())


@router.message(F.text == "👉 В главное меню")
async def get_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
