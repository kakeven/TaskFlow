from fastapi import APIRouter, Depends, status, HTTPException
from dependencies.dependency import get_session
from schemas.user_schemas import User_schema,User_schemaResponse,Login_schema
from sqlalchemy.orm import Session
from services.user_service import criar_user,login

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
class CredenciaisInvalidas(Exception):
    pass

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"adwd"}

@auth_router.post("/criar_conta",response_model=User_schemaResponse)
async def criar_conta(user_schema: User_schema , session: Session = Depends(get_session) ):
    try: 
       return criar_user(user_schema,session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
   

@auth_router.post("/login")
async def login_route(login_schema: Login_schema,session: Session=Depends(get_session)):
    try:
        return login(login_schema,session)
    except CredenciaisInvalidas:
        raise HTTPException(status_code=401,detail="Credenciais invalidas")