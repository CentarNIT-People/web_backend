from deta import Deta
from hashlib import sha256
import httpx
from collections import Counter
from .getip import getIp

deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")
db = deta.Base("users")


def get_all():
    return db.fetch().items


def create_user(request):
    percentages = []
    languages = [x["language"] for x in httpx.get(
        f"https://api.github.com/users/{request.github}/repos").json()]

    for name, pct in {x: int(float(y) / len(languages) * 100)
                      for x, y in Counter(languages).items()}.items():
        percentages.append({"lang   uage": name, "percentage": pct})
    request.languages = sorted(
        percentages, key=lambda d: d['percentage'])[::-1][0:3]
    request.password = sha256(request.password.encode("utf-8")).hexdigest()
    request.flag = "https://countryflagsapi.com/svg/rs"
    request.ip = getIp()
    return db.put(dict(request), key=request.username)


def find_user(username):
    user = db.get(username)
    return user or 404


def change_user(request):
    return db.put(dict(request), key=request.username)


def delete_user(username):
    return db.delete(username)
