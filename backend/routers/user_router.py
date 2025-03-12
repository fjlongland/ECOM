from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels


router = APIRouter(prefix="/users", 
                   tags=["users"])


@router.get("/test")
def test_user_rout(db: Session = Depends(get_db)):
    return{"Users": "Works"}

@router.post("/")
def new_user(db: Session = Depends(get_db)):

    new_user = dbModels.User(user_name = 'test username',
                             user_password = 'test passeord',)
    
    db.add(new_user)
    db.commit()

    return{"test user": "crested"}

@router.delete("/{id}")
def delete_user(id: int, 
                db: Session = Depends(get_db)):

    delete_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    if delete_user == None:
        print("no users in table")

    db.delete(delete_user)
    db.commit()

    return {f"User {id}": "Deleted"}

