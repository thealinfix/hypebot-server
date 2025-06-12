from fastapi import APIRouter
from src.core.constants import SOURCES

router = APIRouter()

@router.get("/")
async def get_sources():
   return {"sources": SOURCES}
