from aiogram.fsm.state import State, StatesGroup


class BackRq(StatesGroup):
    first_last_name = State()
    phone_number = State()
    message = State()
