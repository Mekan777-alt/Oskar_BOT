import asyncio
import mimetypes
from io import BytesIO

from keyboard.main import main_keyboard
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.cartKazahstan import cart_kazahstan
from context.cart_kazahstan_context import GetInfo
from sqlalchemy import select
from config import session, bot
from data.base import KazahstanCart
from aiogram.types import FSInputFile, InputFile

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
    await message.answer("Пожалуйста, введите вашу фамилию:")
    await state.set_state(GetInfo.last_name)


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
    await message.answer("Будет отправляться сообщение такого формата куда-то в канал или в чат личку или в группу")
    await asyncio.sleep(1)
    await message.answer(f"ИМЯ - {data['first_name']}\n"
                         f"ФАМИЛИЯ - {data['last_name']}\n"
                         f"ОТЧЕСТВО - {data['patronymic']}\n"
                         f"ТЕЛЕФОН НОМЕР - {data['phone_number']}\n"
                         f"ИИН(налоговый номер Казахстана) - {data['IIN']}", reply_markup=main_keyboard())
    await message.answer("Еще будет сообщение пользователю по типу все успешно отправилось ожидайте звонка или тп")
    await state.clear()


@router.message(F.text == "👉 Инструкция по получению ИИН")
async def get_instructions_IIN(message: types.Message):
    data_from_db = session.scalar(select(KazahstanCart))
    message_from_db = data_from_db.item1_2_message
    reference_from_db = data_from_db.item1_2_reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db if reference_from_db else ''}",
                         reply_markup=main_keyboard())
    if data_from_db.item1_2_document:
        file_content = data_from_db.item1_2_document['content_type']
        file_io = BytesIO(file_content)
        file_io.seek(0)  # Reset the buffer to the beginning
        file_content_type, _ = mimetypes.guess_type(file_content)
        file = FSInputFile(filename="document.pdf")
        await bot.send_document(chat_id=message.from_user.id, document=file)


@router.message(F.text == "👉 Ссылка на получение документов для налоговой и разъяснения")
async def send_request_(message: types.Message):
    data_from_db = session.scalar(select(KazahstanCart))
    message_from_db = data_from_db.item1_3_message
    reference_from_db = data_from_db.item1_3_reference
    await message.answer(f"{message_from_db}\n\n{reference_from_db if reference_from_db else ''}",
                         reply_markup=main_keyboard())


@router.message(F.text == "👉 В главное меню")
async def get_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_keyboard())