import os
from schemas.user import User
from utils.validation import user_creation
from database.data_access.users import UsersLayer
from utils import github, hashed, send_mail, exceptions, constants

user_exceptions = exceptions.UserExceptions
data_layer = UsersLayer()


class UserLogic:

    @staticmethod
    def _parse_user(user: User):
        user.avatar = github.get_github_avatar_url(user.github)
        user.languages = github.get_github_language_percentages(user.github)
        user.password = hashed.hashed_password(user.password)
        user.is_active = False
        user.status = constants.USER_STATUS["ON_HOLD"]
        user.role = constants.USER_ROLES["STUDENT"]
        email = send_mail.Email("hamzaplojovic9@gmail.com", user.email,
                                os.environ["SMTP_PASSWORD"])
        email.send_code()
        user = dict(user)
        user["_id"] = user["username"]

        return user

    @staticmethod
    def _user_in_db(user: dict):
        user_in_db = {
            "username": user["username"],
            "full_name": user["full_name"],
            "email": user["email"],
            "job": user["job"],
            "languages": user["languages"],
            "avatar": user["avatar"],
            "is_active": user["is_active"],
            "role": user["role"],
            "status": user["status"],
        }

        return user_in_db

    def get_all_users(self) -> list[dict]:
        try:
            return [self._user_in_db(x) for x in data_layer.get_all_users()]
        except (RuntimeError, TypeError, NameError):
            return user_exceptions.raise_conflict("Cannot get users")

    def create_user(self, user: User) -> any:
        if user_creation.validate_existence(user) is not False:
            return user_exceptions.raise_conflict("User already exists")
        try:
            parsed_user = self._parse_user(user)
            data_layer.create_user(parsed_user)
        except (ValueError, TypeError, RuntimeError):
            return user_exceptions.raise_conflict("Cannot create user")

    @staticmethod
    def find_user_by_username(username: str):
        try:
            user = data_layer.get_user_by_username(username)
            return user
        except (SyntaxError, TypeError, RuntimeError):
            return user_exceptions.raise_not_found("User not found")

    @staticmethod
    def update_user(user: User):
        try:
            user.password = hashed.hashed_password(user.password)
            data_layer.update_user("username", dict(user))
        except (NameError, TypeError, RuntimeError):
            return user_exceptions.raise_conflict("Cannot update user")

    @staticmethod
    def delete_user(username: str):
        try:
            data_layer.delete_user(username)
        except (TypeError, NameError, RuntimeError):
            return user_exceptions.raise_conflict("Cannot delete user")

    @staticmethod
    def hard_delete_user(username: str):
        try:
            data_layer.hard_delete_user(username)
        except (SyntaxError, TypeError, RuntimeError):
            return user_exceptions.raise_conflict("Cannot delete user")

    @staticmethod
    def login(username: str, password: str):
        try:
            return data_layer.login(username, password)
        except (RuntimeError, TypeError, NameError):
            return user_exceptions.raise_not_found("User not found")
