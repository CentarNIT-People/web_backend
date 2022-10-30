from datetime import timedelta
from fastapi import Depends, Request
from db.deta_db import connect_to_deta_db
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from utils.jwt_handler import get_username_from_current_user, create_access_token


db = connect_to_deta_db("users")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(request:Request, _:str = Depends(oauth2_scheme)):
    return db.get(get_username_from_current_user(request))


def login(form_data: OAuth2PasswordRequestForm):
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"username": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def approve_code(username:str) -> str:
    user = db.get(username)
    user["status"] = "received"
    db.put(user, key=username)
    return f"Approved {username} that has confirmed email address"