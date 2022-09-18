from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    email: str
    age: str
    status: str
    avatar: str


class User(UserBase):
    class Config:
        orm_mode = True
