from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
deta = Deta("a063wuxg_XANyaMGJ2N31vCkZaPv5NnD7J7SqPD5s")


@app.get("/")
def home():
    return "/docs"
