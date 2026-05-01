from models.task_model import Task,EnumPriority,EnumStatus
from models.user_model import Users
from services.task_service import criar_task
from unittest.mock import MagicMock, patch
import pytest
from schemas.task_schema import Task_schema


@pytest.mark.parametrize("side_effect, esperado", [
    ([0, 0],None),
    ([1, 1],None),
    ([2, 2], ValueError),
])
def test_criar_task(side_effect,esperado):
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


