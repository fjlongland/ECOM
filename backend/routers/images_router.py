import os
from fastapi import APIRouter, Depends, UploadFile, File, Form, Response, status
from sqlalchemy.orm import Session
from database.database import get_db
from database import dbModels


router = APIRouter(prefix="/images",
                   tags=["images"])


#Definses where 9images are stored after they are uploaded:
#NOTE: before launching application this will be changed to a cloud storage location.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))

Upload_Dir = os.path.join(BASE_DIR, "static", "uploaded_images")

os.makedirs(Upload_Dir, exist_ok=True)



#important endpoint users to display images on the frontend.
@router.get("/{id}")
def get_images(id: int,
               db: Session=Depends(get_db)):
    
    images = db.query(dbModels.Image).filter(dbModels.Image.post_id_fk == id).all()

    return images



#endpoint used to add a new image to a post.
#TODO: create new dir for each user to neaten up image storage(You dont want file soup in the storage loc)
#NOTE: file storage can be made even more clean by saving each posts images in their own dir under the user.
@router.post("/")
def add_image(db: Session = Depends(get_db),
              image: UploadFile = File(...),
              post_id: int = Form(...)):
    
    image_path = os.path.join(Upload_Dir, image.filename)

    with open(image_path, "wb") as f:
        f.write(image.file.read())
        loc = f"static/uploaded_images/{image.filename}"
    
    new_image = dbModels.Image(post_id_fk=post_id,
                               image_loc=loc)
    
    db.add(new_image)
    db.commit()
    db.refresh(new_image)

    return {"image_id": new_image.image_id}



#Endpoint used ro remove an image from a post.
#NOTE: deleting an image does not remove the image from the storage location.
@router.delete("/{id}")
def delete_image(id: int,
                 db: Session=Depends(get_db)):
    
    del_image = db.query(dbModels.Image).filter(dbModels.Image.image_id == id).first()

    if del_image is None:
        print("No such image in db");

    db.delete(del_image)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)