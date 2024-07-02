from config import session
from sqlalchemy import text


async def insert_data(data):
    query = text("""INSERT INTO admin_panel_requestuser 
               (first_name, last_name, patronymic, phone_number, iin) 
               VALUES (:first_name, :last_name, :patronymic, :phone_number, :IIN)""")
    await session.execute(query,
                          {"first_name": data['first_name'],
                           "last_name": data['last_name'],
                           "patronymic": data['patronymic'],
                           "phone_number": data['phone_number'],
                           "IIN": data['IIN']})
