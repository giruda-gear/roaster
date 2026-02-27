from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from app.core.auth import create_access_token, hash_password, verify_password
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register(self, user_in: UserCreate):
        if self.db.query(User).filter(User.email == user_in.email).first():
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="email already taken"
            )

        user = User(email=user_in.email, password=hash_password(user_in.password))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def login(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="invalid credentials",
            )
            
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]
