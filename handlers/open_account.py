from keyboard.main import main_keyboard
from aiogram import Router, F, types
from keyboard.open_account import open_account_markup
from config import bot
from db.repository.open_account3_1 import message_for_open_account3_1, get_document3_1, get_document_reserved3_1
from db.repository.open_account3_2 import message_for_open_account3_2, get_document3_2, get_document_reserved3_2
from .settings import delete_file, download_file
from aiogram.types import FSInputFile


router = Router()


@router.message(F.text == "👉 Открытие счетов")
async def open_account(message: types.Message):
    await message.answer("Тут описание раздела", reply_markup=open_account_markup())


@router.message(F.text == "👉 АМ")
async def get_AM(message: types.Message):
    message_text = message_for_open_account3_1()
    if len(message_text) > 2:
        await message.answer(text=message_text, reply_markup=main_keyboard())
        await bot.send_chat_action(chat_id=message.from_user.id, action="upload_document")

    else:
        await message.answer(text="Заполните данные в админке", reply_markup=main_keyboard())
    document_url = get_document3_1()
    if document_url:
        local_filename = str(document_url).split('/')[-1]
        try:
            file_down = await download_file(f"http://91.142.74.227:8000/media/{document_url}", local_filename)
            send_file = FSInputFile(file_down)
            await bot.send_document(chat_id=message.from_user.id, document=send_file)
        except Exception as e:
            await message.answer(text=f"Ошибка загрузки документа: {e}")
        finally:
            await delete_file(local_filename)

    document_reserved_url = get_document_reserved3_1()
    if document_reserved_url:
        local_filename = str(document_reserved_url).split('/')[-1]
        try:
            file_down = await download_file(f"http://91.142.74.227:8000/media/{document_reserved_url}", local_filename)
            send_file = FSInputFile(file_down)
            await bot.send_document(chat_id=message.from_user.id, document=send_file)
        except Exception as e:
            await message.answer(text=f"Ошибка загрузки документа: {e}")
        finally:
            await delete_file(local_filename)



@router.message(F.text == "👉 Казахстан")
async def get_kz(message: types.Message):
    message_text = message_for_open_account3_2()
    if len(message_text) > 2:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    document_url = get_document3_2()
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

    document_reserved_url = get_document_reserved3_2()
    if document_reserved_url:
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


@router.message(F.text == "👉 В главное меню")
async def back_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
    