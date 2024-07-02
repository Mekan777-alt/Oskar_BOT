from datetime import datetime

from config import session
from sqlalchemy import text


async def insert_data(data):
    query = text("""INSERT INTO admin_panel_requestuser 
                   (first_name, last_name, patronymic, phone_number, iin, created_at) 
                   VALUES (:first_name, :last_name, :patronymic, :phone_number, :iin, :created_at)""")
    await session.execute(query,
                          {"first_name": data['first_name'],
                           "last_name": data['last_name'],
                           "patronymic": data['patronymic'],
                           "phone_number": data['phone_number'],
                           "iin": data['IIN'],
                           "created_at": datetime.now()})
