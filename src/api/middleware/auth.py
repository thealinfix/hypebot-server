from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from src.core.config import settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
   if not api_key or api_key != settings.API_KEY:
       raise HTTPException(status_code=403, detail="Invalid API Key")
   return api_key
