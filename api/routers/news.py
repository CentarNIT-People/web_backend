from fastapi import APIRouter, status
from schemas import article
from repo import news

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_news():
    return news.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_news(request: article.Article):
    return news.create_news(request)


@router.put('/{title}', status_code=status.HTTP_202_ACCEPTED)
async def change_news(title, request: article.Article):
    return news.change_news(request, title)


@router.delete('/{title}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(title):
    return news.delete_article(title)


@router.get("/{title}", status_code=status.HTTP_200_OK)
async def get_news_by_title(title):
    return news.get_article_by_title(title)
