from fastapi import APIRouter, status
from schemas import project
from repo import projects

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/")
async def get_all_projects():
    return "/td"
