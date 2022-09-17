from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    age: str


class User(UserBase):
    class Config:
        orm_mode = True
