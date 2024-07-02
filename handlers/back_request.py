from config import bot, send_message_to_group
from keyboard.main import main_keyboard
from aiogram import Router, F, types
from context.back_rq import BackRq
from aiogram.fsm.context import FSMContext
from keyboard.back_rq import back_rq_markup

router = Router()


@router.message(F.text == "👉 Обратная связь")
async def open_chat(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, введите ваше ФИО", reply_markup=back_rq_markup())
    await state.set_state(BackRq.first_last_name)


@router.message(F.text == "👉 Отменить")
async def cancel_chat(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено!", reply_markup=main_keyboard())


@router.message(BackRq.first_last_name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(first_last_name=message.text)
    await message.answer("Введите телефон номер для связи")
    await state.set_state(BackRq.phone_number)


@router.message(BackRq.phone_number)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Введите тест обращение")
    await state.set_state(BackRq.message)


@router.message(BackRq.message)
async def get_message(message: types.Message, state: FSMContext):
    await state.update_data(message=message.text)
    data = await state.get_data()

    text = (f"ФИО: {data['first_last_name']}\n"
            f"Телефон номер: {data['phone_number']}\n\n"
            f"Текст обращение: {data['message']}"
            )
    await bot.send_message(chat_id=send_message_to_group, text=text)
    await state.clear()
    await message.answer("Ваше обращение принято\n\n"
                         "В ближайшее время мы свяжемся с вами для уточнения деталей. ", reply_markup=main_keyboard())
