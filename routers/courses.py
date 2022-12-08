from repo import courses
from schemas import course
from fastapi import BackgroundTasks
from repo.role_checker import RoleChecker
from fastapi import APIRouter, status, Depends

allowed_roles = RoleChecker(["admin", "instructor"])

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_courses() -> list:
    return courses.get_all()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_course(
    request: course.Course,
    background_tasks: BackgroundTasks,
    _=Depends(allowed_roles)) -> course.Course:
    background_tasks.add_task(courses.create_course, request)
    return request


@router.get("/{course_name}", status_code=status.HTTP_200_OK)
async def get_course_by_name(course_name) -> course.Course or 404:
    return courses.get_by_name(course_name)


@router.put("/{course_name}", status_code=status.HTTP_202_ACCEPTED)
async def update_course(
    request: course.Course,
    background_tasks: BackgroundTasks,
    _=Depends(allowed_roles)) -> course.Course:
    background_tasks.add_task(courses.update_course, request)
    return request


@router.delete("/{course_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_name,
                        background_tasks: BackgroundTasks,
                        _=Depends(allowed_roles)):
    background_tasks.add_task(courses.delete_course, course_name)
    return f"{course_name} deleted"


@router.delete("/{course_name}/hard", status_code=status.HTTP_204_NO_CONTENT)
async def hard_delete_course(course_name: str,
                             background_tasks: BackgroundTasks,
                             _=Depends(allowed_roles)):
    background_tasks.add_task(courses.hard_delete_course, course_name)
    return f"{course_name} deleted"


@router.post("/{course_name}/assign", status_code=status.HTTP_202_ACCEPTED)
async def assign_user_to_course(course_name,
                                username,
                                _=Depends(allowed_roles)):
    return courses.courses_action_on_user(course_name, username, "assign")


@router.delete("/{course_name}/remove", status_code=status.HTTP_202_ACCEPTED)
async def remove_user_from_course(course_name,
                                  username,
                                  _=Depends(allowed_roles)):
    return courses.courses_action_on_user(course_name, username, "assign")



@router.get("/{course_name}/students", status_code=status.HTTP_200_OK)
async def get_students_from_course(name: str):
    return courses.get_students_from_course(name)


@router.post("/{course_name}/add_lecture", status_code=status.HTTP_201_CREATED)
async def add_lecture(course_name: str, lecture_details: course.Lecture,
                      background_tasks: BackgroundTasks):
    background_tasks.add_task(courses.add_lecture, course_name,
                              lecture_details)
    return lecture_details


@router.get("/{course_name}/start_lecture", status_code=status.HTTP_200_OK)
async def start_lecture(course_name: str, lecture_name: str,
                        background_tasks: BackgroundTasks):
    background_tasks.add_task(courses.start_lecture, course_name, lecture_name)
    return f"Lecture {lecture_name} has started"


@router.get("/{course_name}/end_lecture", status_code=status.HTTP_200_OK)
async def end_lecture(course_name: str, lecture_name: str,
                      background_tasks: BackgroundTasks):
    background_tasks.add_task(courses.complete_lecture, course_name,
                              lecture_name)
    return f"Lecture {lecture_name} has ended"


@router.post("/{course_name}/{lecture_name}/present")
async def user_presence(request: course.Presence,
                        background_tasks: BackgroundTasks):
    background_tasks.add_task(courses.user_presence, request)
    return request.username + " is present at lecture: " + request.lecture_name + " at course: " + request.course_name
