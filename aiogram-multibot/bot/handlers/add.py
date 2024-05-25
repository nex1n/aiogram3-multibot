from typing import Any


from aiogram import Bot, F, Router

from aiogram.exceptions import TelegramUnauthorizedError
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.utils import is_bot_token
from config import OTHER_BOTS_URL

router = Router()



@router.message(Command("start"))
async def start(message: Message):
    await message.answer('Дарова')

@router.message(Command("add", magic=F.args.func(is_bot_token)))
async def command_add_bot(message: Message, command: CommandObject, bot: Bot) -> Any:
    new_bot = Bot(token=command.args, session=bot.session)
    try:
        bot_user = await new_bot.get_me()
    except TelegramUnauthorizedError:
        return message.answer("Invalid token")
    await new_bot.delete_webhook(drop_pending_updates=True)
    await new_bot.set_webhook(OTHER_BOTS_URL.format(bot_token=command.args))
