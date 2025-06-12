from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.database import Base

class Source(Base):
    __tablename__ = "sources"
    
    key = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # rss, json
    api_url = Column(String, nullable=False)
    category = Column(String, default="sneakers")
    
    is_active = Column(Boolean, default=True)
    check_interval = Column(Integer, default=1800)
    
    last_checked_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    posts = relationship("Post", back_populates="source")
