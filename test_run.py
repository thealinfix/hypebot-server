import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = "7511712960:AAFJ_-2yoeCuHJqwya-MMWu_7-3HNZNePWI"
ADMIN_ID = 361833263

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👟 HypeBot Server готов!\n\nСистема работает корректно.")
    else:
        await message.answer("👟 HypeBot - мониторинг релизов кроссовок")

@dp.message(Command("status"))
async def status_command(message: Message):
    await message.answer(
        "📊 Статус системы:\n\n"
        "✅ Бот: Работает\n"
        "✅ Сервер: Готов к запуску\n"
        "⏳ База данных: Настраивается\n"
        "⏳ Redis: Настраивается"
    )

async def main():
    logging.info("Starting test bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
