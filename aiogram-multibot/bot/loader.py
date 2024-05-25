from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


from config import MAIN_BOT_TOKEN
from loader import session

storage = MemoryStorage()

bot_settings = {"session": session, "parse_mode": ParseMode.HTML}
bot = Bot(token=MAIN_BOT_TOKEN, **bot_settings)
dp = Dispatcher(storage=storage)
