from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserResponse
from app.services.auth import AuthServiceDep


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserCreate, status_code=status.HTTP_201_CREATED
)
def register(user_in: UserCreate, service: AuthServiceDep):
    return service.register(user_in)


@router.post("/login", response_model=UserResponse)
def login(service: AuthServiceDep, form_data: OAuth2PasswordRequestForm = Depends()):
    return service.login(email=form_data.username, password=form_data.password)
