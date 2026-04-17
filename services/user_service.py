from models.user_model import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def criar_user(user_schema, session:Session):
    
    user = session.query(Users).filter(Users.email==user_schema.email).first()
    if user:
        raise ValueError("email ja cadastrado")
    else: 
        password_crypto = bcrypt_context.hash(user_schema.password)
        new_user = Users(name=user_schema.name,email=user_schema.email,password=password_crypto)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

