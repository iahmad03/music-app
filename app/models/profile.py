from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    bio = Column(Text, nullable=True)
    spotify_link = Column(String, nullable=True)
    instagram_link = Column(String, nullable=True)
    twitter_link = Column(String, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="profile")