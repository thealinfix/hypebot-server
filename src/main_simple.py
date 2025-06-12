import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from aiogram import Bot, Dispatcher

# Минимальная конфигурация
TELEGRAM_TOKEN = "7511712960:AAFJ_-2yoeCuHJqwya-MMWu_7-3HNZNePWI"
PORT = 8000

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting HypeBot Server...")
    
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    
    # Установка webhook
    await bot.delete_webhook(drop_pending_updates=True)
    
    app.state.bot = bot
    app.state.dp = dp
    
    yield
    
    print("Shutting down...")
    await bot.session.close()

app = FastAPI(
    title="HypeBot Server",
    version="2.0.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"status": "HypeBot Server is running!"}

@app.get("/api/v1/health")
async def health():
    return {"status": "ok", "service": "HypeBot Server"}

@app.post("/api/v1/webhooks/telegram")
async def telegram_webhook(request: dict):
    # Простая обработка webhook
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
