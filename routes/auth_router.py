from fastapi import APIRouter, Depends
from models.model import Users , db
from sqlalchemy.orm import sessionmaker
from dependencies.dependency import get_session

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"adwd"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str ,password:str,nome:str, session = Depends(get_session) ):
    
    user = session.query(Users).filter(Users.email==email).first()

    if user:
        return {"mensagem":"User ja possui cadastro"}
    else: 
        new_user = Users(name=nome,email=email,password=password)
        session.add(new_user)
        session.commit()
        return {"mensagem":"User cadastrado com sucesso"}