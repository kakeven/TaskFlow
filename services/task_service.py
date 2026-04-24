from sqlalchemy.orm import Session
from models.task_model import Task,EnumPriority,EnumStatus
from models.user_model import Users
from sqlalchemy import or_
from datetime import date
from sqlalchemy import func

def criar_task(task_schema ,session:Session,user:Users):
    if task_schema.title=="":
        raise ValueError("Obrigatorio ter title")
    if task_schema.priority=="":
        raise ValueError("Obrigatorio ter priority")
    

    task_count = session.query(func.count(Task.id)).filter(
            Task.user_id == user.id,
            or_(
                Task.status == EnumStatus.in_progress,
                Task.status == EnumStatus.pending
            )
        ).scalar()

    task_high_count = session.query(func.count(Task.id)).filter(
        Task.user_id == user.id,
        Task.priority == EnumPriority.high
        ).scalar()

    if task_count>=5:
        raise ValueError("Complete outras tarefas primeiro")
    
    if task_schema.priority==EnumPriority.high and task_high_count>=2:
        raise ValueError("Limite de tarefas high atingido")
    

    if task_schema.due_date and task_schema.due_date <= date.today():
        raise ValueError("Datas devem ser no futuro")

    new_task=Task(title=task_schema.title,
                  description=task_schema.description,
                  status=task_schema.status,
                  priority=task_schema.priority,
                  due_date=task_schema.due_date,
                  user_id=user.id)


    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task


def ver_tarefas_listas(user,session:Session):
    task = session.query(Task).filter(Task.user_id==user.id).all()
    if not task:
        raise ValueError("Nenhuma task criada")
    return task

def ver_tarefa_id(id_task,session:Session,user):
    task = session.query(Task).filter(Task.id==id_task, Task.user_id==user.id).first()
    if not task:
        raise ValueError("Task não encontrada")
    return task

def editar_tarefa_id(id_task,session,user,task_schema_update):
    task = ver_tarefa_id(id_task,session,user)

    update_data = task_schema_update.dict(exclude_unset=True)
    if task.status.order()>task_schema_update.status.order():
        raise ValueError("Não é permitido retroceder")

    for campo,valor in update_data.items():
        setattr(task,campo,valor)
    session.commit()
    session.refresh(task)

    return task

def excluir_tarefa_id(id_task,session:Session,user):
    task = ver_tarefa_id(id_task,session,user)
    
    
    session.delete(task)
    session.commit()
    return task