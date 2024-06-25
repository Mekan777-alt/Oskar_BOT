from config import session
from sqlalchemy import text


def get_message():
    message = session.execute(text("""SELECT message FROM admin_panel_gotochat""")).first()
    return message[0] if message else ''


def get_reference():
    reference = session.execute(text("""SELECT reference FROM admin_panel_gotochat""")).first()
    return reference[0] if reference else ''


def message_for_go_to_chat():
    message = get_message()
    reference = get_reference()

    message_text = f"{message}\n\n{reference}"

    return message_text
