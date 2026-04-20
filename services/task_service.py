from sqlalchemy.orm import Session
from models.task_model import Task

def criar_task(task_schema ,session:Session):
    if task_schema.title=="":
        raise ValueError("Obrigatorio ter title")
    if task_schema.priority=="":
        raise ValueError("Obrigatorio ter priority")

    new_task=Task(title=task_schema.title,
                  description=task_schema.description,
                  status=task_schema.status,
                  priority=task_schema.priority,
                  due_date=task_schema.due_date,
                  user_id=task_schema.user_id)


    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task