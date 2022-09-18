from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    age: str
    password: str


class User(UserBase):
    class Config:
        orm_mode = True
