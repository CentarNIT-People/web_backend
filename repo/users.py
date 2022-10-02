from hashlib import sha256
import httpx
from schemas import user
from utils import github
from deta import Base

db = Base("users")


def get_all():
    return db.fetch().items


def create_user(user: user.User):
    user.avatar = github.get_github_avatar_url(user.github)
    user.languages = github.get_github_language_percentages(user.github)
    user.password = sha256(user.password.encode("utf-8")).hexdigest()
    user.is_active = False

    return db.put(dict(user), key=user.email)


def find_user_by_username(username):
    user = db.get(username)
    return user or 404

def change_user(request):
    return db.put(dict(request), key=request.username)


def delete_user(username):
    return db.delete(username)
