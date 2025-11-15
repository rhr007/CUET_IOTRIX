from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db import get_db
from models import User
from auth import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(name: str, phone: str, password: str, session: Session = Depends(get_db)):
    existing = session.exec(select(User).where(User.phone == phone)).first()
    if existing:
        raise HTTPException(400, "Phone already registered")

    user = User(
        name=name,
        phone=phone,
        password=hash_password(password),
        is_admin=False,
        is_active=False   # admin must approve
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "Signup complete, waiting for admin approval"}

@router.post("/login")
def login(phone: str, password: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.phone == phone)).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(401, "Invalid credentials")

    if not user.is_active:
        raise HTTPException(403, "Account not approved by admin")

    return {"message": "Login successful", "is_admin": user.is_admin, "user_id": user.id}
