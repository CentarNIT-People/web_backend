from fastapi import HTTPException, status
from deta import Deta

deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")
db = deta.Base("admin")


def login(username, password):
    user = [x for x in db.fetch().items if x["username"] ==
            username and x["password"] == password]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User not found!")
    return 200
