from deta import Deta
from hashlib import sha256

deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")
db = deta.Base("users")


def login(username, password):
    user = db.fetch({"username": username, "password": sha256(
        password.encode("utf-8")).hexdigest()})
    return 200 if user else 404
