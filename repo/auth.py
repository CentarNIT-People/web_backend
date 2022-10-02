from hashlib import sha256
from deta import Base

db = Base("users")


def login(username, password):
    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items[0]
    return 200 if user else 404
