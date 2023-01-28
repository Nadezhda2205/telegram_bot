from bot_app.local_settings import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())
