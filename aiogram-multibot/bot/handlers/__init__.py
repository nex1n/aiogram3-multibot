from aiogram import Router


def setup_routers() -> Router:
    from bot.handlers import add
    router = Router()
    router.include_routers(
        add.router,
    )
    return router