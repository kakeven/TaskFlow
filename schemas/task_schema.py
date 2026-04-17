from pydantic import BaseModel
from datetime import date
from models.task_model import EnumPriority,EnumStatus


class Task_schema(BaseModel):
    title:str
    description: str | None = None
    priority: EnumPriority
    status: EnumStatus
    due_date: date | None = None
    user_id: int

    class Config:
        from_attributes = True