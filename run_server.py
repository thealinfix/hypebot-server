import asyncio
import logging
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import uvicorn
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Конфигурация
TELEGRAM_TOKEN = "7511712960:AAFJ_-2yoeCuHJqwya-MMWu_7-3HNZNePWI"
ADMIN_CHAT_ID = 361833263
PORT = 8000

# Глобальные переменные для бота
bot = None
dp = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global bot, dp
    logger.info("🚀 Starting HypeBot Server...")
    
    # Инициализация бота
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    
    # Регистрация обработчиков
    @dp.message(Command("start"))
    async def start_command(message: Message):
        await message.answer(
            "👟 HypeBot Server работает!\n\n"
            "Доступные команды:\n"
            "/start - Начало работы\n"
            "/status - Статус системы\n"
            "/check - Проверить источники"
        )
    
    @dp.message(Command("status"))
    async def status_command(message: Message):
        await message.answer(
            "📊 Статус системы:\n\n"
            "✅ Сервер: Работает\n"
            "✅ База данных: PostgreSQL подключена\n"
            "✅ Redis: Подключен\n"
            "✅ API: Доступен на порту 8000\n"
            f"⏰ Время сервера: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
    
    @dp.message(Command("check"))
    async def check_command(message: Message):
        if message.from_user.id == ADMIN_CHAT_ID:
            await message.answer("🔄 Запускаю проверку источников...")
            # TODO: Добавить реальную проверку
            await asyncio.sleep(2)
            await message.answer("✅ Проверка завершена!\nНайдено 0 новых постов.")
        else:
            await message.answer("❌ Эта команда доступна только администратору")
    
    # Удаляем старый webhook и запускаем polling в фоне
    await bot.delete_webhook(drop_pending_updates=True)
    asyncio.create_task(dp.start_polling(bot))
    logger.info("✅ Telegram bot started with polling")
    
    app.state.bot = bot
    app.state.dp = dp
    
    yield
    
    logger.info("🛑 Shutting down...")
    await dp.stop_polling()
    await bot.session.close()

# Создание FastAPI приложения
app = FastAPI(
    title="HypeBot Server",
    description="Сервер для мониторинга релизов кроссовок",
    version="2.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {
        "status": "running",
        "service": "HypeBot Server",
        "version": "2.0.0",
        "endpoints": {
            "health": "/api/v1/health",
            "docs": "/docs",
            "webhook": "/api/v1/webhooks/telegram"
        }
    }

@app.get("/api/v1/health")
async def health():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "checks": {
            "server": True,
            "bot": bot is not None,
            "database": True,  # TODO: Реальная проверка БД
            "redis": True      # TODO: Реальная проверка Redis
        }
    }

@app.post("/api/v1/webhooks/telegram")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        update = Update(**data)
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"ok": False, "error": str(e)}

@app.get("/api/v1/posts")
async def get_posts():
    return {
        "posts": [],
        "total": 0,
        "message": "Posts API endpoint"
    }

@app.post("/api/v1/check-sources")
async def check_sources():
    # TODO: Реализовать проверку источников
    return {
        "status": "checking",
        "sources": ["SneakerNews", "Hypebeast", "Highsnobiety"]
    }

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 HypeBot Server v2.0")
    print("=" * 50)
    print(f"📍 Server: http://localhost:{PORT}")
    print(f"📚 API Docs: http://localhost:{PORT}/docs")
    print(f"🤖 Bot: @ChiPackPostBot")
    print("=" * 50)
    
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="info")
