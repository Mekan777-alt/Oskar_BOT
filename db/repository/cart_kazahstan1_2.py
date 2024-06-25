from config import session
from sqlalchemy import text


def get_message1_2():
    message = session.execute(text("""SELECT item1_2_message FROM admin_panel_kazahstancart1_2""")).first()
    return message[0] if message else ''


def get_reference1_2():
    reference = session.execute(text("""SELECT item1_2_reference FROM admin_panel_kazahstancart1_2""")).first()
    return reference[0] if reference else ''


def get_document1_2():
    document = session.execute(text("""SELECT item1_2_document FROM admin_panel_kazahstancart1_2""")).first()
    return document[0] if document else None


def get_document_reserved1_2():
    document = session.execute(text("""SELECT item1_2_document_reserve FROM admin_panel_kazahstancart1_2""")).first()
    return document[0] if document else None


def message_for_cart_kazahstan1_2():
    message = get_message1_2()
    reference = get_reference1_2()

    message_text = f"{message}\n\n{reference}"

    return message_text
