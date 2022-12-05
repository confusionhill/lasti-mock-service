from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class User_Register(BaseModel):
    fullname: str
    username: str
    password: str

class Update_Tutor_Avail(BaseModel):
    available_from: str
    untill: str