from fastapi import APIRouter
from datetime import datetime
from src.core.database import engine
from src.core.redis import get_redis

router = APIRouter()

@router.get("/")
async def health_check():
    """Проверка здоровья сервиса"""
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "HypeBot Server"
    }

@router.get("/ready")
async def readiness_check():
    """Проверка готовности сервиса"""
    checks = {
        "database": False,
        "redis": False
    }
    
    # Проверка БД
    try:
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        checks["database"] = True
    except:
        pass
    
    # Проверка Redis
    try:
        redis = await get_redis()
        await redis.ping()
        checks["redis"] = True
    except:
        pass
    
    all_ready = all(checks.values())
    return {
        "ready": all_ready,
        "checks": checks
    }
