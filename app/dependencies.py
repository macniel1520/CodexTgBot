from aiogram import Bot, Dispatcher
from openai import OpenAI

from .config import settings

bot = Bot(token=settings.telegram_token)
dp = Dispatcher()
openai_client = OpenAI(api_key=settings.chatgpt_api_key)
