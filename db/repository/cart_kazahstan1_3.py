from config import session
from sqlalchemy import text


def get_message1_3():
    message = session.execute(text("""SELECT item1_3_message FROM admin_panel_kazahstancart1_3""")).first()
    return message[0] if message else ''


def get_reference1_3():
    reference = session.execute(text("""SELECT item1_3_reference FROM admin_panel_kazahstancart1_3""")).first()
    return reference[0] if reference else ''


def get_document1_3():
    document = session.execute(text("""SELECT item1_3_document FROM admin_panel_kazahstancart1_3""")).first()
    if document:
        if len(document[0]) > 1:
            return document[0]
    return None


def get_document_reserved1_3():
    document = session.execute(text("""SELECT item1_3_document_reserve FROM admin_panel_kazahstancart1_3""")).first()
    if document:
        if len(document[0]) > 1:
            return document[0]
    return None


def message_for_cart_kazahstan1_3():
    message = get_message1_3()
    reference = get_reference1_3()

    message_text = f"{message}\n\n{reference}"

    return message_text
