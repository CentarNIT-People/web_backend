from fastapi import APIRouter, status
from repo import login


router = APIRouter(
    prefix="/account",
    tags=["Account"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
def login_user(username, password):
    return login.login(username, password)
