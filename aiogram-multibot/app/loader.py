from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from loader import session


storage = MemoryStorage()

bot_settings = {"session": session, "parse_mode": ParseMode.HTML}
dp = Dispatcher(storage=storage)
