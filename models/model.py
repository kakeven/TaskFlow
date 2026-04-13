from sqlalchemy import create_engine, Column,String,ForeignKey,Integer,DateTime,Date,Enum as SQLenum
from sqlalchemy.orm import declarative_base
from enum import Enum

from datetime import datetime

#cria a conexao
db = create_engine("sqlite:///database/banco.db")

#cria a base do banco de dados
Base = declarative_base()

#criar classes/tabelas do banco
"""""
TASK
USERS
"""

class Users(Base):
    __tablename__ = "users"

    id= Column("id",Integer, nullable=False,primary_key=True,autoincrement=True)
    name = Column("name",String, nullable=False)
    email = Column("email",String, nullable=False)
    password = Column("password",String, nullable=False)
    created_at = Column(DateTime,default=datetime.now)

    def __init__(self,name,email,password,created_at):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at




class EnumPriority(str,Enum): 
    low = "low"
    medium = "medium" 
    high = "high"
    
class EnumStatus(str,Enum): 
    pending = "pending" 
    in_progress = "in_progress" 
    done = "done"

class Task(Base):

    __tablename__ = "tasks"




    id = Column(Integer, nullable=False,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    description = Column(String)
    priority = Column(SQLenum(EnumPriority),nullable=False)
    status = Column(SQLenum(EnumStatus))
    due_date = Column(Date)
    user_id = Column(ForeignKey("users.id"),nullable=False)

    def __init__(self,title,priority,user_id,status=EnumStatus.pending,description=None,due_date=None):
        self.title = title
        self.priority = priority
        self.status = status
        self.user_id = user_id
        self.description = description
        self.due_date = due_date