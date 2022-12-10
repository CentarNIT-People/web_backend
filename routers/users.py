from repo import users
from schemas import user
from fastapi import BackgroundTasks
from repo.role_checker import RoleChecker
from fastapi import APIRouter, Depends, status

allowed_roles = RoleChecker(["admin"])

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users() -> list:
    return users.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(request: user.User) -> user.User or dict:
    return users.create_user(request)


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def find_user(username: str) -> user.User or 404:
    return users.find_user_by_username(username)


@router.put("/{username}", status_code=status.HTTP_202_ACCEPTED)
async def change_user(
    request: user.User,
    background_tasks: BackgroundTasks,
    _=Depends(allowed_roles)
) -> user.User or dict:
    background_tasks.add_task(users.update_user, request)
    return request


@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def soft_delete_user(username: str,
                           background_tasks: BackgroundTasks,
                           _=Depends(allowed_roles)):
    background_tasks.add_task(users.delete_user, username)
    return f"User with username {username} deleted from database"


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def hard_delete_user(username: str,
                           background_tasks: BackgroundTasks,
                           _=Depends(allowed_roles)):
    background_tasks.add_task(users.hard_delete_user, username)
    return f"User with username {username} deleted from database"


@router.get("/login", status_code=status.HTTP_200_OK)
async def user_login(username: str, password: str):
    return users.login(username, password)
