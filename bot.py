import asyncio
import base64
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Greet the user on /start."""
    await message.answer(
        "Привет! Я бот-диетолог. Отправь мне фото еды — я определю блюдо и пришлю калории, белки, жиры и углеводы на 100 грамм."
    )


@dp.message(F.photo)
async def handle_photo(message: Message) -> None:
    """Handle incoming photos and analyze them with OpenAI Vision."""
    try:
        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)
        file_bytes = await bot.download_file(file.file_path)
        b64_image = base64.b64encode(file_bytes.read()).decode("utf-8")

        prompt = (
            "Определи блюдо на фотографии и рассчитай его КБЖУ на 100 грамм. "
            "Формат ответа:\n"
            "Название: ...\n"
            "Калории: ... ккал\n"
            "Белки: ... г\n"
            "Жиры: ... г\n"
            "Углеводы: ... г\n"
            "Значения указаны на 100 г"
        )

        def ask_openai() -> str:
            response = client.responses.create(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system",
                        "content": (
                            "Ты - диетолог. Определи блюдо на фото и рассчитай его КБЖУ на 100 г."
                        ),
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": prompt},
                            {"type": "input_image", "image_base64": b64_image},
                        ],
                    },
                ],
            )
            return response.output_text.strip()

        result = await asyncio.to_thread(ask_openai)
        await message.answer(result)
    except Exception:
        await message.answer("Не удалось распознать блюдо. Попробуй другое фото.")


async def main() -> None:
    """Start the bot."""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
