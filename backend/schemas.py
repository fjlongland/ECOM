from pydantic import BaseModel

class BasicUser(BaseModel):
    user_name: str
    user_password: str

    class Config:
        orm_mode = True

