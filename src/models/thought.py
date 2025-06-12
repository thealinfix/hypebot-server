from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from src.core.database import Base

class Thought(Base):
    __tablename__ = "thoughts"
    
    id = Column(Integer, primary_key=True)
    topic = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    
    image_url = Column(String)
    image_description = Column(Text)
    
    hashtags = Column(JSON, default=list)
    
    is_published = Column(Boolean, default=False)
    published_at = Column(DateTime(timezone=True))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
