import os

from typing import List
from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels
from .. import schemas

router = APIRouter(prefix="/posts",
                   tags=["posts"])

# @router.get("/test")
# def test():
#     return{"posts": "works"}

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))

Upload_Dir = os.path.join(BASE_DIR, "static", "uploaded_images")
os.makedirs(Upload_Dir, exist_ok=True)



#TODO: add frontend calls
#TODO: add response model for all crud operations
#TODO: add all http responses



#create a new user
@router.post("/", response_model = schemas.createPostResponse)
def new_post(db: Session = Depends(get_db),
             title: str = Form(...),
             content: str = Form(...),
             user_id: int = Form(...),
             images: List[UploadFile] = File(...)):
    

    new_post = dbModels.Post(post_title=title,
                             post_content=content,
                             user_id_fk=user_id)
    
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    for image in images:
        image_path = os.path.join(Upload_Dir, image.filename)
        with open(image_path, "wb") as f:
            f.write(image.file.read())

        loc_retrieve = f"static/uploaded_images/{image.filename}"

        new_image = dbModels.Image(image_loc=loc_retrieve, post_id_fk = new_post.post_id )

        db.add(new_image)

    db.commit()
    
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
                db: Session = Depends(get_db), 
                title: str = Form(...), 
                content: str = Form(...)):
    update_post = db.query(dbModels.Post).filter(dbModels.Post.post_id == id).first()
    print(title, content)
    if update_post == None:
        print("post does not exhist")
    
    update_post.post_title = title
    update_post.post_content = content

    db.commit()

    return {"post_id": update_post.post_id}


#delete a single user
@router.delete("/{id}")
def delete_post(id: int,
                db: Session = Depends(get_db)):
    
    delete_post = db.query(dbModels.Post).filter(dbModels.Post.post_id == id).first()

    if delete_post == None:
        print("post does not exhist.")

    db.delete(delete_post)
    db.commit()

    return{f"post {id}": "Deleted"}

@router.get("/")
def get_all_posts(db: Session = Depends(get_db)):

    posts = db.query(dbModels.Post).all()

    return posts

@router.get("/user/{id}")
def get_user_posts(id: int,
                   db: Session = Depends(get_db)):
    
    posts = db.query(dbModels.Post).filter(dbModels.Post.user_id_fk == id).all()

    return posts