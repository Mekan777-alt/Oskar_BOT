from aiogram.fsm.state import State, StatesGroup


class GetInfo(StatesGroup):
    FIO = State()
    phone_number = State()
    IIN = State()
