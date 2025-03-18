from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels

router = APIRouter(prefix="/images",
                   tags=["images"])

@router.get("/{id}")
def get_images(id: int,
               db: Session=Depends(get_db)):

    images = db.query(dbModels.Image).filter(dbModels.Image.post_id_fk == id).all()

    return images


