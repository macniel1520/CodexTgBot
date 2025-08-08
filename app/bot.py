from .dependencies import bot, dp
from .handlers import router


def register_handlers() -> None:
    dp.include_router(router)


async def run_bot() -> None:
    register_handlers()
    await dp.start_polling(bot)
