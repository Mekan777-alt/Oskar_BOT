from aiogram.fsm.state import State, StatesGroup


class GetInfo(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
    phone_number = State()
    email = State()
    IIN = State()
