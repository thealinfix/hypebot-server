import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.api.routes import (
    posts, sources, generation, schedule, 
    webhooks, admin, health
)
from src.core.config import settings
from src.core.database import init_db
from src.core.redis import init_redis
from src.core.logger import setup_logger
from src.services.scrapers.scheduler_service import SchedulerService
from src.bot.handlers import setup_bot_handlers
from aiogram import Bot, Dispatcher

logger = setup_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения"""
    logger.info("Starting HypeBot Server...")
    
    await init_db()
    await init_redis()
    
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dp = Dispatcher()
    setup_bot_handlers(dp)
    
    await bot.set_webhook(f"{settings.BASE_URL}/api/v1/webhooks/telegram")
    
    scheduler = SchedulerService()
    asyncio.create_task(scheduler.start())
    
    app.state.bot = bot
    app.state.dp = dp
    app.state.scheduler = scheduler
    
    yield
    
    logger.info("Shutting down HypeBot Server...")
    await scheduler.stop()
    await bot.delete_webhook()
    await bot.session.close()

app = FastAPI(
    title="HypeBot Server",
    description="Сервер для мониторинга релизов кроссовок и уличной моды",
    version="2.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
app.include_router(webhooks.router, prefix="/api/v1/webhooks", tags=["webhooks"])
app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(sources.router, prefix="/api/v1/sources", tags=["sources"])
app.include_router(generation.router, prefix="/api/v1/generation", tags=["generation"])
app.include_router(schedule.router, prefix="/api/v1/schedule", tags=["schedule"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG
    )
