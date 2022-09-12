from fastapi import HTTPException, status
from deta import Deta

deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")
db = deta.Base("projects")


def get_all():
    return db.fetch().items


def create_project(request):
    return db.put(dict(request), key=request.name)


def change_project(request, name):
    project = [x for x in db.fetch().items if x["name"] == name][0]
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with name {name} not found!")
    return db.put(dict(request), key=name)


def delete_project(name):
    project = [x for x in db.fetch().items if x["name"] == name][0]
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with name {name} not found!")
    return db.delete(project["key"])


def get_project_by_name(name):
    project = [x for x in db.fetch().items if x["name"] == name][0]
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project with name {name} not found!")
    return project
