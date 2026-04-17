#uvicorn main:app --reload
#main -> arquivo que roda | app-> nome dado a variavel do fastapi
from fastapi import FastAPI

from routes.auth_router import auth_router
from routes.task_router import task_router



app = FastAPI()
app.include_router(auth_router)
app.include_router(task_router)

