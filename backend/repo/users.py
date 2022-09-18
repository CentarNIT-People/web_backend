from deta import Deta

deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")
db = deta.Base("users")


def get_all():
    return db.fetch().items


def create_user(request):
    return db.put(dict(request), key=request.username)


def find_user(username):
    user = db.get(username)
    return user if user else 404


def change_user(request):
    return db.put(dict(request), key=request.username)


def delete_user(username):
    return db.delete(username)
