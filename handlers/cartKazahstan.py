from keyboard.main import main_keyboard
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.cartKazahstan import cart_kazahstan, cancel_cart_kazahstan
from context.cart_kazahstan_context import GetInfo
from config import bot, send_message
from db.repository.cart_kazahstan1_2 import get_document1_2, get_document_reserved1_2, message_for_cart_kazahstan1_2
from db.repository.cart_kazahstan1_3 import get_document1_3, get_document_reserved1_3, message_for_cart_kazahstan1_3
from .settings import download_file, delete_file
from aiogram.types import FSInputFile

router = Router()


@router.message(F.text == "👉 Карта Казахстана")
async def get_cart(message: types.Message):
    await message.answer("Тут будет какое-то описание данного раздела", reply_markup=cart_kazahstan())


@router.message(F.text == "👉 Инструкция по открытию есть ИИН/НЕТ ИИН")
async def get_inform_user(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, введите ваше имя:", reply_markup=types.ReplyKeyboardRemove())

    await state.set_state(GetInfo.first_name)


@router.message(GetInfo.first_name)
async def get_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Пожалуйста, введите вашу фамилию:", reply_markup=cart_kazahstan())
    await state.set_state(GetInfo.last_name)


@router.message(F.text == "👉 Отменить")
async def cancel_cart(message: types.Message, state: FSMContext):
    await message.answer("Отменено!", reply_markup=cart_kazahstan())
    await state.clear()


@router.message(GetInfo.last_name)
async def get_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Пожалуйста, введите ваше отчество:")
    await state.set_state(GetInfo.patronymic)


@router.message(GetInfo.patronymic)
async def get_patronymic(message: types.Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    await message.answer("Пожалуйста, введите ваш номер телефона:")
    await state.set_state(GetInfo.phone_number)


@router.message(GetInfo.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Пожалуйста, введите ИИН(налоговый номер Казахстана)")
    await state.set_state(GetInfo.IIN)


@router.message(GetInfo.IIN)
async def get_IIN(message: types.Message, state: FSMContext):
    await state.update_data(IIN=message.text)
    data = await state.get_data()

    await bot.send_message(chat_id=send_message,
                           text=f"ИМЯ - {data['first_name']}\n"
                                f"ФАМИЛИЯ - {data['last_name']}\n"
                                f"ОТЧЕСТВО - {data['patronymic']}\n"
                                f"ТЕЛЕФОН НОМЕР - {data['phone_number']}\n"
                                f"ИИН(налоговый номер Казахстана) - {data['IIN']}")
    await message.answer("Заявка успешно отправлена", reply_markup=main_keyboard())
    await state.clear()


@router.message(F.text == "👉 Инструкция по получению ИИН")
async def get_instructions_IIN(message: types.Message):
    message_text = message_for_cart_kazahstan1_2()
    if len(message_text) > 2:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    document_url = get_document1_2()
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

    document_reserved_url = get_document_reserved1_2()
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


@router.message(F.text == "👉 Ссылка на получение документов для налоговой и разъяснения")
async def send_request_(message: types.Message):
    message_text = message_for_cart_kazahstan1_3()
    if len(message_text) > 2:
        await message.answer(text=message_text, reply_markup=main_keyboard())
    else:
        await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    document_url = get_document1_3()
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

    document_reserved_url = get_document_reserved1_3()
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


@router.message(F.text == "👉 В главное меню")
async def get_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())
