from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

#cria a conexao
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/banco.db")

# Render às vezes gera com "postgres://" em vez de "postgresql://"
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

db = create_engine(DATABASE_URL)

#cria a base do banco de dados
Base = declarative_base()