from pydantic import BaseModel


class Article(BaseModel):
    title: str
    description: str
    date: str
    image: str
    author: str
