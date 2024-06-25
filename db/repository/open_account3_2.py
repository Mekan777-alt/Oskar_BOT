from config import session
from sqlalchemy import text


def get_message3_2():
    message = session.execute(text("""SELECT item3_2_message FROM admin_panel_openaccount3_2""")).first()
    return message[0] if message else ''


def get_reference3_2():
    reference = session.execute(text("""SELECT item3_2_reference FROM admin_panel_openaccount3_2""")).first()
    return reference[0] if reference else ''


def get_document3_2():
    document = session.execute(text("""SELECT item3_2_document FROM admin_panel_openaccount3_2""")).first()
    if len(document[0]) > 1:
        return document[0]
    else:
        return None


def get_document_reserved3_2():
    document = session.execute(text("""SELECT item3_2_document_reserve FROM admin_panel_openaccount3_2""")).first()
    if len(document[0]) > 1:
        return document[0]
    else:
        return None


def message_for_open_account3_2():
    message = get_message3_2()
    reference = get_reference3_2()

    message_text = f"{message}\n\n{reference}"

    return message_text
