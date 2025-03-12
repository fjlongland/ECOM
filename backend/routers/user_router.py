from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels

#create the router for the user table
router = APIRouter(prefix="/users", 
                   tags=["users"])




#just for testing the user table connection
@router.get("/test")
def test_user_rout(db: Session = Depends(get_db)):
    return{"Users": "Works"}



#create a new user
#TODO: add hashing for passwords
#TODO: add a response model
@router.post("/")
def new_user(db: Session = Depends(get_db)):

    new_user = dbModels.User(user_name = 'test username',
                             user_password = 'test passeord',)
    
    db.add(new_user)
    db.commit()

    return{"test user": "crested"}



#get one user
#TODO: add a response model
@router.get("/{id}")
def get_user(id: int,
             db: Session = Depends(get_db)):
    
    get_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    return(get_user)




#update a user
#TODO: add userCreate model
@router.put("/{id}")
def update_user(id: int, 
                db: Session = Depends(get_db)):
    
    update_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    if update_user == None:
        print("User does not exist")

    update_user.user_name="updated username"
    update_user.user_password="updated password"

    db.commit()

    return{f"user {id}": "updated"}






#delete a user
#TODO: add HTTP return
@router.delete("/{id}")
def delete_user(id: int, 
                db: Session = Depends(get_db)):

    delete_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    if delete_user == None:
        print("no users in table")

    db.delete(delete_user)
    db.commit()

    return {f"User {id}": "Deleted"}

