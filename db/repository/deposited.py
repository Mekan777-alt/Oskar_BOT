from config import session
from sqlalchemy import text


def get_message():
    message = session.execute(text("""SELECT item2_1_message FROM admin_panel_deposited""")).first()
    return message[0] if message else ''


def get_reference():
    reference = session.execute(text("""SELECT item2_1_reference FROM admin_panel_deposited""")).first()
    return reference[0] if reference else ''


def get_document():
    document = session.execute(text("""SELECT item2_1_document FROM admin_panel_deposited""")).first()
    return document[0] if document else None


def get_document_reserved():
    document = session.execute(text("""SELECT item2_1_document_reserve FROM admin_panel_deposited""")).first()
    return document[0] if document else None


def message_for_deposited():
    message = get_message()
    reference = get_reference()

    message_text = f"{message}\n\n{reference}"

    return message_text
