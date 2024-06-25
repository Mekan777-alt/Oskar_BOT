from config import session
from sqlalchemy import text


def get_message3_1():
    message = session.execute(text("""SELECT item3_1_message FROM admin_panel_openaccount3_1""")).first()
    return message[0] if message else ''


def get_reference3_1():
    reference = session.execute(text("""SELECT item3_1_reference FROM admin_panel_openaccount3_1""")).first()
    return reference[0] if reference else ''


def get_document3_1():
    document = session.execute(text("""SELECT item3_1_document FROM admin_panel_openaccount3_1""")).first()
    return document[0] if document else None


def get_document_reserved3_1():
    document = session.execute(text("""SELECT item3_1_document_reserve FROM admin_panel_openaccount3_1""")).first()
    return document[0] if document else None


def message_for_open_account3_1():
    message = get_message3_1()
    reference = get_reference3_1()

    message_text = f"{message}\n\n{reference}"

    return message_text
