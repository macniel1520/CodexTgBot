import asyncio
import base64

from aiogram import F, Router
from aiogram.types import Message

from app.dependencies import bot, openai_client

router = Router()


@router.message(F.photo)
async def handle_photo(message: Message) -> None:
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
            response = openai_client.responses.create(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system",
                        "content": "Ты - диетолог. Определи блюдо на фото и рассчитай его КБЖУ на 100 г.",
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
