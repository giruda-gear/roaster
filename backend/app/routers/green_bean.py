from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.green_bean import GreenBean
from app.schemas.green_bean import GreenBeanCreate, GreenBeanResponse


router = APIRouter(prefix="/admin/green_beans", tags=["admin"])


@router.post("", response_model=GreenBeanResponse)
def create_green_bean(data: GreenBeanCreate, db: Session = Depends(get_db)):
    green_bean = GreenBean(**data.model_dump())
    db.add(green_bean)
    db.commit()
    db.refresh(green_bean)
    return green_bean


@router.get("")
def get_green_beans(db: Session = Depends(get_db)):
    return db.query(GreenBean).all()
