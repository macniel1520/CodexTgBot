from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Привет! Я бот-диетолог. Отправь мне фото еды — я определю блюдо и пришлю калории, белки, жиры и углеводы на 100 грамм."
    )
