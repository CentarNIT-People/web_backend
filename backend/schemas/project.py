from pydantic import BaseModel


class Project(BaseModel):
    name: str
    link: str
    language: str
