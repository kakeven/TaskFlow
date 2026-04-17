from fastapi import APIRouter, Depends, status, HTTPException
from models.model import Users
from dependencies.dependency import get_session
from dotenv import load_dotenv
import os
from passlib.context import CryptContext
from schemas.user_schemas import User_schema
from sqlalchemy.orm import Session

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


load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"adwd"}

@auth_router.post("/criar_conta")
async def criar_conta(user_schema: User_schema , session: Session = Depends(get_session) ):
    
    user = session.query(Users).filter(Users.email==user_schema.email).first()
    if user:
        raise HTTPException(status_code=400,detail="Email ja cadastrado")
    else: 
        password_crypto = bcrypt_context.hash(user_schema.password)
        new_user = Users(name=user_schema.name,email=user_schema.email,password=password_crypto)
        session.add(new_user)
        session.commit()
        return {"mensagem":"User cadastrado com sucesso"}