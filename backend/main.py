from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, projects, news

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(news.router)
