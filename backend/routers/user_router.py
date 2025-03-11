from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db


router = APIRouter(prefix="/users", 
                   tags=["users"])


@router.get("/test")
def test_user_rout(db: Session = Depends(get_db)):
    return{"Users": "Works"}