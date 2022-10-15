from typing import Optional
from pydantic import BaseModel,EmailStr


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    github: str
    email: EmailStr
    phone_number:str
    job: str
    role: str
    status:str
    is_active: str



class User(UserBase):
    avatar: Optional[str] = None
    languages: Optional[list] = None
    approved_at: Optional[str] = None
    rejected_at: Optional[str] = None
    rejected_counter:Optional[int] = 0
