from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    token: str


class ShowUser(BaseModel):
    username: str
    email: str
    phone: str


class User(UserBase):
    class Config:
        orm_mode = True
