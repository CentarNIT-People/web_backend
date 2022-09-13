from fastapi import HTTPException, status
from deta import Deta
from hashlib import sha256

deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")
db = deta.Base("users")


def get_users():
    return db.fetch().items


def create_user(request):
    request.password = sha256(request.password.encode('utf-8')).hexdigest()
    return db.put(dict(request), key=request.username)


def change_user(request, name):
    user = [x for x in db.fetch().items if x["name"] == name][0]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with name {name} not found!")
    return db.put(dict(request), key=name)


def delete_user(name):
    user = [x for x in db.fetch().items if x["name"] == name][0]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with name {name} not found!")
    return db.delete(user["key"])


def get_user(name):
    user = [x for x in db.fetch().items if x["name"] == name][0]
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with name {name} not found!")
    return user
