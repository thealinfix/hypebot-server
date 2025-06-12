from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(String, primary_key=True)
    title = Column(String(200), nullable=False)
    link = Column(String, nullable=False, unique=True)
    description = Column(Text)
    context = Column(Text)
    source_key = Column(String, ForeignKey("sources.key"))
    category = Column(String, default="sneakers")
    
    images = Column(JSON, default=list)
    original_images = Column(JSON, default=list)
    tags = Column(JSON, default=dict)
    
    is_published = Column(Boolean, default=False)
    is_pending = Column(Boolean, default=True)
    is_favorite = Column(Boolean, default=False)
    needs_parsing = Column(Boolean, default=True)
    
    published_at = Column(DateTime(timezone=True))
    scheduled_at = Column(DateTime(timezone=True))
    source_published_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    source = relationship("Source", back_populates="posts")
    generated_images = relationship("GeneratedImage", back_populates="post", cascade="all, delete-orphan")
    schedules = relationship("Schedule", back_populates="post", cascade="all, delete-orphan")
