import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()


DATABASE_FILE = "db.sqlite"
UPLOAD_DIR = "upload/"
ENGINE_URI = "sqlite:///" + DATABASE_FILE

engine = create_engine(ENGINE_URI, echo=False)
session = Session(engine)

token = os.getenv('TOKEN')
bot = Bot(token=token)

dp = Dispatcher(bot=bot, storage=MemoryStorage())
