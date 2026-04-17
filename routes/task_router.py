from fastapi import APIRouter,Depends
from dependencies.dependency import get_session
from sqlalchemy.orm import Session
from schemas.task_schema import Task_schema

task_router = APIRouter(prefix="/task",tags=["task"])

@task_router.post("/criar")
async def criar_pedido(task_schema: Task_schema,session: Session = Depends(get_session)):
    ...
