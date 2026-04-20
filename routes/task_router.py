from fastapi import APIRouter,Depends, HTTPException
from dependencies.dependency import get_session
from sqlalchemy.orm import Session
from schemas.task_schema import Task_schema
from services.task_service import criar_task



task_router = APIRouter(prefix="/task",tags=["task"])

@task_router.post("/criar")
async def criar_tarefa(task_schema: Task_schema,session: Session = Depends(get_session)):
    try:
        return criar_task(task_schema,session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
