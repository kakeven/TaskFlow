#uvicorn main:app --reload
#main -> arquivo que roda | app-> nome dado a variavel do fastapi
from fastapi import FastAPI

from routes.auth_router import auth_router
from routes.task_router import task_router
from routes.user_route import user_router
from database.conection import db, Base
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=db)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # link do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(task_router)

