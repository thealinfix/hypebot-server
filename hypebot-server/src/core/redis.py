import redis.asyncio as redis
from src.core.config import settings
from src.core.logger import logger

redis_client = None

async def init_redis():
    global redis_client
    try:
        redis_client = await redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
        await redis_client.ping()
        logger.info("Redis connected successfully")
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {e}")
        raise

async def get_redis():
    return redis_client

def get_key(key: str) -> str:
    """Получить ключ с префиксом"""
    return f"{settings.REDIS_PREFIX}{key}"
