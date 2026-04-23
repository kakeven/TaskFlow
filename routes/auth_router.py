from fastapi import APIRouter, Depends, HTTPException
from dependencies.dependency import get_session
from schemas.user_schemas import User_schema,User_schemaResponse,Login_schema
from sqlalchemy.orm import Session
from services.user_service import criar_user,login,CredenciaisInvalidas,verificar_token,criar_token
from models.user_model import Users
from fastapi.security import  OAuth2PasswordRequestForm


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


auth_router = APIRouter(prefix="/auth",tags=["auth"])


@auth_router.post("/criar_conta",response_model=User_schemaResponse)
async def criar_conta(user_schema: User_schema , session: Session = Depends(get_session) ):
    try: 
       return criar_user(user_schema,session)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
   

@auth_router.post("/login")
async def login_route( form_data: OAuth2PasswordRequestForm = Depends(),session: Session=Depends(get_session)):
    try:
        
        return login(form_data,session)
    except CredenciaisInvalidas:
        raise HTTPException(status_code=401,detail="Credenciais invalidas")
    



@auth_router.get("/refresh")
async def refresh_token(user:Users = Depends(verificar_token)):
    access_token = criar_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
    
    