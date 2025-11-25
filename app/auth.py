from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import app.models, app.schemas, app.hashing
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=app.schemas.UserOut)
def register(user: app.schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if username/email already exists
    if db.query(app.models.User).filter(app.models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    if db.query(app.models.User).filter(app.models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = app.hashing.hash_password(user.password)
    new_user = app.models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
