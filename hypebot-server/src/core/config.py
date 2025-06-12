from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # App
    APP_NAME: str = "HypeBot Server"
    DEBUG: bool = False
    PORT: int = 8000
    BASE_URL: str
    SECRET_KEY: str
    API_KEY: str
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # Telegram
    TELEGRAM_TOKEN: str
    TELEGRAM_CHANNEL: str = "@channelusername"
    ADMIN_CHAT_ID: Optional[int] = None
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/hypebot"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_PREFIX: str = "hypebot:"
    
    # Scheduler
    CHECK_INTERVAL_SECONDS: int = 1800
    MAX_PENDING_POSTS: int = 100
    MAX_POST_AGE_DAYS: int = 7
    MAX_IMAGES_PER_POST: int = 10
    
    # Timezone
    DEFAULT_TIMEZONE: str = "Europe/Moscow"
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
