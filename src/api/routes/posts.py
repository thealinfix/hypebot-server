from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.core.database import get_db
from src.models.post import Post
from src.schemas.post import PostResponse, PostCreate
from src.services.post_service import PostService

router = APIRouter()

@router.get("/", response_model=List[PostResponse])
async def get_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    is_pending: Optional[bool] = None,
    is_favorite: Optional[bool] = None,
    category: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Получить список постов"""
    service = PostService(db)
    posts = await service.get_posts(
        skip=skip,
        limit=limit,
        is_pending=is_pending,
        is_favorite=is_favorite,
        category=category
    )
    return posts

@router.post("/{post_id}/publish")
async def publish_post(
    post_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Опубликовать пост"""
    service = PostService(db)
    result = await service.publish_post(post_id)
    if not result:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"success": True, "post_id": post_id}

@router.post("/{post_id}/favorite")
async def toggle_favorite(
    post_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Добавить/удалить из избранного"""
    service = PostService(db)
    result = await service.toggle_favorite(post_id)
    return {"success": True, "is_favorite": result}
