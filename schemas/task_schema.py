from pydantic import BaseModel
from datetime import date
from models.task_model import EnumPriority,EnumStatus
from typing import Optional

class Task_schema(BaseModel):
    title:str
    description: str | None = None
    priority: EnumPriority
    status: EnumStatus
    due_date: date | None = None
    

    class Config:
        from_attributes = True

class Task_schema_update(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[EnumStatus] = None

    class Config:
        from_attributes = True
    