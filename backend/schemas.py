from pydantic import BaseModel

#TODO add more specific response models later.

class BasicUser(BaseModel):
    user_name: str
    user_password: str

    class Config:
        from_attributes = True



class CreateUserResponse(BaseModel):
    user_id: int

    class Config:
        from_attributes = True

class createPostResponse(BaseModel):
    post_id: int

    class Config:
        from_attributes = True