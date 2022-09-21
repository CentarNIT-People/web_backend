from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    github: str
    email: str
    age: str
    status: str
    avatar: str
    languages: list
    flag: str
    country: str
    city: str


class User(UserBase):
    class Config:
        orm_mode = True
