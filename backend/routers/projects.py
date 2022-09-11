from fastapi import APIRouter, status
from schemas import project
from repo import projects

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_projects():
    return projects.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_project(request: project.Project):
    return projects.create_project(request)


@router.put('/{name}', status_code=status.HTTP_202_ACCEPTED)
async def change_user(name, request: project.Project):
    return projects.change_project(request, name)


@router.delete('/{name}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(name):
    return projects.delete_project(name)


@router.get("/{name}", status_code=status.HTTP_200_OK)
async def get_user_by_name(name):
    return projects.get_project_by_name(name)
