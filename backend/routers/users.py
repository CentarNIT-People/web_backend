from fastapi import APIRouter, status
from repo import users
from schemas import user


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_users():
    return users.get_users()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: user.User):
    return users.create_user(request)


@router.put('/{name}', status_code=status.HTTP_202_ACCEPTED)
async def change_user(name, request: user.User):
    return users.change_user(request, name)


@router.delete('/{name}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(name):
    return users.delete_user(name)
