from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboard.main import main_keyboard, chat_parse
from utils.parse_chanell import is_subscribed


router = Router()


@router.message(Command('start'))
async def start(message: types.Message):
    channel_id = '@OskarCapital'
    if not await is_subscribed(message.from_user.id, channel_id):
        await message.answer('Вы должны подписаться на наш канал, чтобы получить доступ к этому контенту!\n\n'
                             'https://t.me/+cWldq2n39Sw1N2Fi',
                             reply_markup=chat_parse())
    else:
        await message.answer("Здравствуйте, я бот-Capital. \n\n"
                             "Готов тебе помочь с выбором продукта или просто с актуальными новостями, "
                             "чтобы не пропустить важные события на фондовом рынке и всегда быть в курсе торговых "
                             "возможностей. \n\n"
                             "Буду рад помочь!", reply_markup=main_keyboard())


@router.message(F.text == "👉 Подписался")
async def start_parse_chat(message: types.Message):
    channel_id = '-1002158982311'
    if not await is_subscribed(message.from_user.id, channel_id):
        await message.answer('Вы должны подписаться на наш канал, чтобы получить доступ к этому контенту!\n\n'
                             'https://t.me/+cWldq2n39Sw1N2Fi',
                             reply_markup=chat_parse())
    else:
        await message.answer("Здравствуйте, я бот-Capital. \n\n"
                             "Готов тебе помочь с выбором продукта или просто с актуальными новостями, "
                             "чтобы не пропустить важные события на фондовом рынке и всегда быть в курсе торговых "
                             "возможностей. \n\n"
                             "Буду рад помочь!", reply_markup=main_keyboard())
