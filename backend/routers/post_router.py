from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels

router = APIRouter(prefix="/posts",
                   tags=["posts"])

# @router.get("/test")
# def test():
#     return{"posts": "works"}



#TODO: add frontend calls
#TODO: add response model for all crud operations
#TODO: add all http responses



#create a new user
@router.post("/")
def new_post(db: Session = Depends(get_db)):
    new_post = dbModels.Post(post_title="Test Title",
                             post_content="Test Content")
    
    db.add(new_post)
    db.commit()

    return {"post": "created"}


#get a single user
@router.get("/{id}")
def get_post(id: int,
             db: Session = Depends(get_db)):

    get_post = db.query(dbModels.Post).filter(dbModels.Post.post_id == id).first()

    return(get_post)

#update a single user
@router.put("/{id}")
def update_post(id: int,
                db: Session = Depends(get_db)):
    update_post = db.query(dbModels.Post).filter(dbModels.Post.post_id == id).first()

    if update_post == None:
        print("post does not exhist")
    
    update_post.post_title = "updated Title"
    update_post.post_content = "updated Content"

    db.commit()

    return{f"post {id}": "updated"}


#delete a single user
@router.delete("/{id}")
def delete_user(id: int,
                db: Session = Depends(get_db)):
    
    delete_user = db.query(dbModels.Post).filter(dbModels.Post.post_id == id).first()

    if delete_user == None:
        print("post does not exhist.")

    db.delete(delete_user)
    db.commit()

    return{f"post {id}": "Deleted"}