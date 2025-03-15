from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels
from .. import schemas

router = APIRouter(prefix="/posts",
                   tags=["posts"])

# @router.get("/test")
# def test():
#     return{"posts": "works"}



#TODO: add frontend calls
#TODO: add response model for all crud operations
#TODO: add all http responses



#create a new user
@router.post("/", response_model = schemas.createPostResponse)
def new_post(db: Session = Depends(get_db),
             title: str = Form(...),
             content: str = Form(...)):
    new_post = dbModels.Post(post_title=title,
                             post_content=content)
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


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