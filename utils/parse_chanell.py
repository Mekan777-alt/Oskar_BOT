from config import bot


async def is_subscribed(chat_id: int, channel_id: str) -> bool:
    chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=chat_id)
    return chat_member.status in ['creator', 'administrator', 'member']
