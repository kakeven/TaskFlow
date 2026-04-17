from sqlalchemy.orm import sessionmaker
from models.user_model import db


def get_session():
    try:
        Session = sessionmaker(bind=db) #conexao com banco de dados
        session = Session() # instancia da conexao
        yield session
    finally:
        session.close()