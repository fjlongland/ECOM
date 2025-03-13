from pydantic import BaseModel

class BasicUser(BaseModel):
    user_name: str
    user_password: str

    class Config:
        from_attributes = True



class CreateResponse(BaseModel):
    user_id: int

    class Config:
        from_attributes = True