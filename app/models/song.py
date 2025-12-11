from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class SongCategory(Base):
    __tablename__ = "song_categories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)  # "Song of the Year", "Gym Song", etc.
    is_default = Column(Boolean, default=False)  # True for fixed categories
    position = Column(Integer, default=0)  # For ordering
    
    # Relationships
    user = relationship("User", back_populates="song_categories")
    songs = relationship("SongEntry", back_populates="category", cascade="all, delete-orphan")


class SongEntry(Base):
    __tablename__ = "song_entries"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("song_categories.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    spotify_link = Column(String, nullable=True)
    position = Column(Integer, default=0)  # For ordering within category
    
    # Relationships
    category = relationship("SongCategory", back_populates="songs")