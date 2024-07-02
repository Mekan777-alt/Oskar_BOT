import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("POST_USER")
password = os.getenv("POST_PASSWORD")
host = os.getenv("POST_HOST")
port = os.getenv("POST_PORT")
database = os.getenv("POST_DB")


ENGINE_URI = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(ENGINE_URI, echo=False)
session = Session(engine)

token = os.getenv('TOKEN')
bot = Bot(token=token)

dp = Dispatcher(bot=bot, storage=MemoryStorage())

send_message = os.getenv("SEND_MESSAGE")
