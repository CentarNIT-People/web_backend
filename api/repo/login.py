from fastapi import status, HTTPException
from deta import Deta
from hashlib import sha256
from routers import token
from datetime import timedelta

deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")
db = deta.Base("users")
ACCESS_TOKEN_EXPIRE_MINUTES = 1440


def login(username, password):
    user = [x for x in db.fetch().items if x["username"] == username][0]
    if user and user["password"] == sha256(password.encode('utf-8')).hexdigest():
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = token.create_access_token(
            data={"sub": user["username"]}, expires_delta=access_token_expires
        )
        user["token"] = access_token
        return user
    raise HTTPException(
        detail="User with not found!", status_code=status.HTTP_404_NOT_FOUND)
