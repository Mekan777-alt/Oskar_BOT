from config import session
from sqlalchemy import text


def get_cartKazahstan_3_1():
    data = session.execute(text("""SELECT * FROM admin_panel_openaccount""")).all()
    return [data[0][0][1], data[0][0][2]]


a = get_cartKazahstan_3_1()
print(a)