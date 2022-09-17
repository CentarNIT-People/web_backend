from fastapi import FastAPI
from deta import Deta

app = FastAPI()
deta = Deta("a063wuxg_k8zsfQrTEriaLdJwXbGRrE5DfcQYuaXd")


@app.get("/")
def home():
    return "HI"
