from sqlalchemy.orm import sessionmaker, Session
from database.conection import db
from models.user_model import Users
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_session():
    try:
        Session = sessionmaker(bind=db) #conexao com banco de dados
        session = Session() # instancia da conexao
        yield session
    finally:
        session.close()

def verificar_token(token:str = Depends(oauth2_scheme),session:Session = Depends(get_session)):
    try:
        secret = SECRET_KEY
        algorithm = ALGORITHM
        if secret is None or algorithm is None:
            raise HTTPException(status_code=401,detail=" Algoritimo ou chave invalidos")
        payload = jwt.decode(token, secret, algorithm)
        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(status_code=401,detail="sub invalido")
        user_id = int(sub)

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user
    