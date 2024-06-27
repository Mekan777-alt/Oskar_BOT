from keyboard.main import main_keyboard
from aiogram import Router, F, types
from db.repository.go_to_chat import get_message, get_reference, message_for_go_to_chat
from config import bot
import aiogram


router = Router()


@router.message(F.text == "👉 Переход в чат")
async def open_chat(message: types.Message):
    pass
    # chat_id = "-1002161715921"
    # user_id = message.from_user.id
    #
    # try:
    #     member = await bot.get_chat_member(chat_id, user_id)
    #     if member.status in ["member", "administrator", "creator"]:
    #         message_text = message_for_go_to_chat()
    #         if len(message_text) > 2:
    #             await message.answer(text=message_text, reply_markup=main_keyboard())
    #         else:
    #             await message.answer(text="Заполните данные в админке", markup=main_keyboard())
    #     else:
    #         await message.answer(text="Вы не подписаны на канал. Подпишитесь, чтобы продолжить.")
    # except Exception as e:
    #     print(e)
