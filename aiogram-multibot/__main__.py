import logging
import sys

from aiohttp import web

from aiogram import Bot, Dispatcher

from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    TokenBasedRequestHandler,
    setup_application,
)

from config import MAIN_BOT_PATH, OTHER_BOTS_PATH, WEB_SERVER_HOST, WEB_SERVER_PORT, BASE_URL
from bot.loader import dp as _main_dp, bot as _main_bot
from app.loader import dp as _app_dp,bot_settings as _app_bot_settings

async def on_startup(dispatcher: Dispatcher, bot: Bot):
    logging.info("Bot started")
    await bot.set_webhook(f"{BASE_URL}{MAIN_BOT_PATH}")


def main():
    logging.basicConfig(level=logging.INFO)
    app = web.Application()

    from bot.handlers import setup_routers
    _main_dp.include_router(setup_routers())
    _main_dp.startup.register(on_startup)
    SimpleRequestHandler(dispatcher=_main_dp, bot=_main_bot).register(app, path=MAIN_BOT_PATH)

    from app.handlers import setup_routers
    _app_dp.include_router(setup_routers())

    TokenBasedRequestHandler(
        dispatcher=_app_dp,
        bot_settings=_app_bot_settings,
    ).register(app, path=OTHER_BOTS_PATH)

    setup_application(app, _main_dp, bot=_main_bot)
    setup_application(app, _app_dp)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
