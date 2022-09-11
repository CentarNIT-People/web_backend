from pydantic import BaseModel


class Article(BaseModel):
    title: str
    description: str
    image: str
    author: str
