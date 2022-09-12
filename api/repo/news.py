from fastapi import HTTPException, status
from deta import Deta

deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")
db = deta.Base("news")


def get_all():
    return db.fetch().items


def create_news(request):
    return db.put(dict(request), key=request.title)


def change_news(request, title):
    article = [x for x in db.fetch().items if x["title"] == title][0]
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with title {title} not found!")
    return db.put(dict(request), key=title)


def delete_article(title):
    article = [x for x in db.fetch().items if x["title"] == title][0]
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with title {title} not found!")
    return db.delete(article["key"])


def get_article_by_title(title):
    article = [x for x in db.fetch().items if x["title"] == title][0]
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with title {title} not found!")
    return article
