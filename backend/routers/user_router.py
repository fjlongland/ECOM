from fastapi import APIRouter, Depends, status, Form, HTTPException, Response
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels
from .. import schemas

#create the router for the user table
router = APIRouter(prefix="/users", 
                   tags=["users"])


#TODO: update response models for returns


#create a new user
#TODO: add hashing for passwords
#TODO: expand user database to add more info on user
@router.post("/", 
             response_model=schemas.CreateUserResponse, 
             status_code=status.HTTP_201_CREATED,
             )

def new_user(db: Session = Depends(get_db), 
             user_name: str = Form(...), 
             user_password: str = Form(...)):

    new_user = dbModels.User(user_name = user_name,
                             user_password = user_password,)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




#get one user
@router.get("/{id}")
def get_user(id: int,
             db: Session = Depends(get_db)):
    
    get_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    return(get_user)




#update a user
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
@router.delete("/{id}")
def delete_user(id: int, 
                db: Session = Depends(get_db)):

    delete_user = db.query(dbModels.User).filter(dbModels.User.user_id == id).first()

    if delete_user == None:
        print("no users in table")

    db.delete(delete_user)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)





#Temporary login for users.
#TODO: NB: need authentication for users!!!!!!!!!!!!!!!!!!!
@router.post("/login")
def userLogin(db: Session = Depends(get_db), 
              username: str = Form(...), 
              password: str = Form(...)):

    attempt_user = db.query(dbModels.User).filter(dbModels.User.user_name == username, 
                                                  dbModels.User.user_password == password
                                                  ).first()

    if not attempt_user:
        print("Invalid login: User not found")

    return {"user_id": attempt_user.user_id, "message": "Login successful"}