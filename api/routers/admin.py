from fastapi import APIRouter, status
from repo import admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/login", status_code=status.HTTP_200_OK)
def login_user(username, password):
    return admin.login(username, password)
