from models.user_model import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone

class CredenciaisInvalidas(Exception):
    pass


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ACESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACESS_TOKEN_EXPIRE_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def criar_token(user_id):
    #JWT -> Json web token
    data_exp = datetime.now(timezone.utc)+timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES) 
    info={
        "sub":user_id,
        "exp":data_exp
    }
    encode_jwt = jwt.encode(info,SECRET_KEY,ALGORITHM)
    
    return encode_jwt

def autenticar_user(email,password,session):
    user = session.query(Users).filter(Users.email==email).first()

    if not user:
        raise CredenciaisInvalidas()
    
    if not bcrypt_context.verify(password,user.password):
        raise CredenciaisInvalidas()

    return user
    

def criar_user(user_schema, session:Session):
    
    user = session.query(Users).filter(Users.email==user_schema.email).first()
    if user:
        raise ValueError("Credencial invalida")
    else: 
        password_crypto = bcrypt_context.hash(user_schema.password)
        new_user = Users(name=user_schema.name,email=user_schema.email,password=password_crypto)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

def login(login_schema,session: Session):
    user = autenticar_user(login_schema.email,login_schema.password,session)
    if user:
        acess_token=criar_token(user.id)
        return {
            "access_token":acess_token,
            "token_type":"Bearer"
        }    
    else:
        raise ValueError ("usuario não encontrado e/ou credenciais invalidas")
