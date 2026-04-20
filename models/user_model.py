from sqlalchemy import Column,String,Integer,DateTime
from database.conection import Base

from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id= Column("id",Integer, nullable=False,primary_key=True,autoincrement=True)
    name = Column("name",String, nullable=False)
    email = Column("email",String, nullable=False)
    password = Column("password",String, nullable=False)
    created_at = Column(DateTime,default=datetime.now)

    def __init__(self,name,email,password,created_at=datetime.now()):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at




