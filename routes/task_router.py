from fastapi import APIRouter

task_router = APIRouter(prefix="/task",tags=["task"])

@task_router.get("/")
async def funcao():
    return "funcao acessada"