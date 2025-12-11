from pydantic import BaseModel

class ProfileUpdate(BaseModel):
    bio: str | None = None
    spotify_link: str | None = None
    instagram_link: str | None = None
    twitter_link: str | None = None

class ProfileResponse(BaseModel):
    id: int
    user_id: int
    bio: str | None
    spotify_link: str | None
    instagram_link: str | None
    twitter_link: str | None

    class Config:
        from_attributes = True