from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
async def get_stats():
   return {"stats": {"posts": 0, "sources": 5}}
