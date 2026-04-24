from fastapi import APIRouter,Depends, HTTPException
from dependencies.dependency import get_session,verificar_token
from sqlalchemy.orm import Session
from schemas.task_schema import Task_schema,Task_schema_update
from services.task_service import criar_task,ver_tarefas_listas,ver_tarefa_id,editar_tarefa_id,excluir_tarefa_id
from models.user_model import Users

"""
200 OK — requisição bem sucedida  
201 Created — recurso criado com sucesso  
204 No Content — sucesso sem conteúdo de resposta  

400 Bad Request — requisição inválida (dados errados)  
401 Unauthorized — não autenticado (sem login/token)  
403 Forbidden — sem permissão (acesso negado)  
404 Not Found — recurso não encontrado  
409 Conflict — conflito (ex: já existe no sistema)  
422 Unprocessable Entity — erro de validação (muito comum no FastAPI)  

500 Internal Server Error — erro interno do servidor  
"""

task_router = APIRouter(prefix="/task",tags=["task"],dependencies=[Depends(verificar_token)])

@task_router.post("/",status_code=201)
async def criar_tarefa(task_schema: Task_schema,session: Session = Depends(get_session),user:Users = Depends(verificar_token)):
    try:
        return criar_task(task_schema,session,user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@task_router.get("/")
async def ver_tarefas(user:Users = Depends(verificar_token),session:Session = Depends(get_session)):
    try: 
        return ver_tarefas_listas(user,session)
    except ValueError as e:
        raise HTTPException(status_code=204,detail=str(e))
    
@task_router.get("/{id_task}")
async def ver_tarefa(id_task:int,session:Session=Depends(get_session),user:Users = Depends(verificar_token)):
    try:
        return ver_tarefa_id(id_task,session,user)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
        
@task_router.patch("/{id_task}")
async def editar_tarefa(id_task:int,task_schema:Task_schema_update,session:Session = Depends(get_session),user : Users=Depends(verificar_token)):
    try:
        return editar_tarefa_id(id_task,session,user,task_schema)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    
@task_router.delete("{id_task}")
async def excluir_tarefa(id_task:int,session:Session = Depends(get_session),user : Users=Depends(verificar_token)):
    try:
        return excluir_tarefa_id(id_task,session,user)
    except ValueError as e:
        HTTPException(status_code=404,detail=str(e))
