from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    @validator("password")
    def password_max_bytes(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must be <= 72 bytes")
        return v

class UserOut(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True
