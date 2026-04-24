from sqlalchemy import  Column,String,ForeignKey,Integer,Date,Enum as SQLenum
from enum import Enum
from database.conection import Base



class EnumPriority(str,Enum): 
    low = "low"
    medium = "medium" 
    high = "high"
    
class EnumStatus(str,Enum): 
    pending = "pending" 
    in_progress = "in_progress" 
    done = "done"

    def order(self):
        return {
            EnumStatus.pending: 1,
            EnumStatus.in_progress: 2,
            EnumStatus.done: 3
        }[self]

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