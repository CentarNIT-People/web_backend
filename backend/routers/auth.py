from fastapi import APIRouter, status
from repo import auth

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
def login(username, password):
    return auth.login(username, password)
