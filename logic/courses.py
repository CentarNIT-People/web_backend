from schemas.course import Course
from database.data_access.users import UsersLayer
from database.data_access.courses import CoursesLayer

data_layer = CoursesLayer()
users_layer = UsersLayer()


class CoursesLogic:

    @staticmethod
    def _parse_course(course: Course):
        course = dict(course)
        course["_id"] = course["name"]
        return course

    def get_all_courses(self) -> list[dict]:
        return data_layer.get_all_courses()

    def get_course_by_name(self, course_name: str):
        return data_layer.get_course_by_name(course_name)

    def create_course(self, course: Course):
        course = self._parse_course(course)
        return data_layer.create_course(course)

    def update_course(self, course: Course):
        return data_layer.update_course(dict(course))

    def delete_course(self, course_name: str):
        return data_layer.delete_course(course_name)

    def hard_delete_course(self, course_name):
        return data_layer.hard_delete_course(course_name)

    def get_students_from_course(self, course_name):
        return data_layer.get_course_by_name(course_name)["students"]

    def courses_action_on_user(self, course_name, username, action):
        course = data_layer.get_course_by_name(course_name)
        user = users_layer.get_user_by_username(username)
        if action == "assign":
            course["students"].append(username)
            user["courses"].append(course_name)
        elif action == "remove":
            course["students"].remove(username)
            user["courses"].remove(course_name)
        else:
            pass
        users_layer.update_user("username", dict(user))
        data_layer.update_course(course)
        return "done"

    def add_lecture_to_course(self, course_name: str, lecture: dict):
        course = data_layer.get_course_by_name(course_name)
        course["plan"].append(dict(lecture))
        return data_layer.update_course(course)

    def change_lecture_status(self, course_name: str, lecture_name: str,
                              lecture_status: str):
        course = data_layer.get_course_by_name(course_name)
        for x in course["plan"]:
            if x["name"] == lecture_name:
                x["status"] = lecture_status
        return data_layer.update_course(course)

    def user_presence(self, request: any):
        course = data_layer.get_course_by_name(request["course_name"])
        for x in course["plan"]:
            if (x["name"] == request["lecture_name"]
                    and x["status"] == "started"):
                present: list = x["present"] if request[
                    "is_present"] is True else x["not_present"]
                not_present: list = x["not_present"] if request[
                    "is_present"] is True else x["present"]
                present.append(request["username"])
                try:
                    not_present.remove(request["username"])
                except (SyntaxError, RuntimeError, ValueError, TypeError):
                    pass
                return data_layer.update_course(course)
        return None
