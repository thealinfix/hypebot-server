from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.core.database import get_db

router = APIRouter()

@router.get("/")
async def get_posts(
   skip: int = Query(0, ge=0),
   limit: int = Query(20, ge=1, le=100),
   db: AsyncSession = Depends(get_db)
):
   return {"posts": [], "total": 0}
