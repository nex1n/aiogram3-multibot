from aiogram import Router

from aiogram.filters import Command, CommandObject
from aiogram.types import Message




router = Router()

@router.message(Command("start"))
async def main_bot_handler(message: Message):
    await message.answer("Hello from daughter bot!")