from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboard.cartKazahstan import cart_kazahstan
from context.cart_kazahstan_context import GetInfo

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
    await message.answer("Пожалуйста, введите ИИН(налоговый номер Казахстана")
    await state.set_state(GetInfo.IIN)


@router.message(GetInfo.IIN)
async def get_IIN(message: types.Message, state: FSMContext):
    await state.update_data(IIN=message.text)



