from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.green_bean import GreenBean


router = APIRouter(prefix="/green_beans", tags=["green_beans"])


@router.get("/")
def get_green_beans(db: Session = Depends(get_db)):
    return db.query(GreenBean).all()
