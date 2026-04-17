from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


#cria a conexao
db = create_engine("sqlite:///database/banco.db")

#cria a base do banco de dados
Base = declarative_base()