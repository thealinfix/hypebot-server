from fastapi import APIRouter, Request, HTTPException
from aiogram.types import Update
from src.core.logger import logger

router = APIRouter()

@router.post("/telegram")
async def telegram_webhook(request: Request):
   try:
       data = await request.json()
       update = Update(**data)
       
       bot = request.app.state.bot
       dp = request.app.state.dp
       
       await dp.feed_update(bot, update)
       
       return {"ok": True}
   except Exception as e:
       logger.error(f"Webhook error: {e}")
       raise HTTPException(status_code=500, detail=str(e))
