from models.task_model import Task,EnumPriority,EnumStatus
from models.user_model import Users
from services.task_service import criar_task,editar_tarefa_id
from unittest.mock import MagicMock, patch
import pytest
from schemas.task_schema import Task_schema
from datetime import date,timedelta

#teste de criar mais de 2 tarefas high
@pytest.mark.parametrize("side_effect, esperado", [
    ([0, 0],None),
    ([1, 1],None),
    ([2, 2], ValueError),
    
])
def test_criar_task_high(side_effect,esperado):
    user = MagicMock()
    user.id = 1

    session = MagicMock()

    session.query.return_value.filter.return_value.scalar.side_effect = side_effect
    task_schema = Task_schema(
        title="Task 1",
        priority=EnumPriority.high,
        status=EnumStatus.pending
    )

    
    if esperado:
        with pytest.raises(ValueError,match="Limite de tarefas high atingido"):
            criar_task(task_schema,session,user)
    else:
        result = criar_task(task_schema,session,user)
        assert result is not None


#teste de criar mais de 5 tarefas
@pytest.mark.parametrize("side_effect, esperado", [
    ([0, 0],None),
    ([1, 0],None),
    ([2, 0],None ),
    ([3, 0],None),
    ([4, 0],None),
    ([5, 0],ValueError),

    
])
def test_criar_task_limite(side_effect,esperado):
    user = MagicMock()
    user.id = 1

    session = MagicMock()

    session.query.return_value.filter.return_value.scalar.side_effect = side_effect
    task_schema = Task_schema(
        title="Task 1",
        priority=EnumPriority.medium,
        status=EnumStatus.pending
    )

    
    if esperado:
        with pytest.raises(ValueError,match="Limite de tarefas atingido"):
            criar_task(task_schema,session,user)
    else:
        result = criar_task(task_schema,session,user)
        assert result is not None


#teste de criar tarefa em data passada ou presente
@pytest.mark.parametrize("side_effect, esperado, due_date", [
    ([0, 0],ValueError,date.today()- timedelta(days=1)),#ontem
    ([0, 0],ValueError,date.today()),# Hoje
    ([0, 0],None,date.today() + timedelta(days=1)),#Amanha
])
def test_editar_data(side_effect,esperado,due_date):
    user = MagicMock()
    user.id = 1

    session = MagicMock()

    session.query.return_value.filter.return_value.scalar.side_effect = side_effect
    task_schema = Task_schema(
        title="Task 1",
        priority=EnumPriority.medium,
        status=EnumStatus.pending,
        due_date= due_date
    )

    
    if esperado:
        with pytest.raises(ValueError,match="Datas devem ser no futuro"):
            criar_task(task_schema,session,user)
    else:
        result = criar_task(task_schema,session,user)
        assert result is not None


