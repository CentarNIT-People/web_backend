from hashlib import sha256
import os
from deta import Base

db = Base("users")

def user_action(username, value):
    user = db.fetch({"username": username}).items[0]
    user["is_active"] = value
    return db.put(user, key=user["username"])


def login(username, password):
    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()}).items
    return 200 if user[0]["role"] == "Admin" else 404
