from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.database import Base

class GeneratedImage(Base):
    __tablename__ = "generated_images"
    
    id = Column(Integer, primary_key=True)
    post_id = Column(String, ForeignKey("posts.id"))
    
    url = Column(String, nullable=False)
    prompt = Column(Text)
    style = Column(String)
    model = Column(String, default="dall-e-3")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    post = relationship("Post", back_populates="generated_images")
