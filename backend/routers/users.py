from fastapi import APIRouter, status
router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/',status_code=status.HTTP_200_OK)
async def get_users():
    return "users"

@router.post('/',status_code=status.HTTP_201_CREATED)
async def get_users():
    return "users"
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def get_users(id):
    return id
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def get_users(id):
    return id