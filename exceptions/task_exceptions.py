from fastapi import HTTPException

class TaskNaoEncontrada(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail={
            "code": "TASK_NOT_FOUND",
            "message": "Task não encontrada"
        })

class LimiteTasksAtingido(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail={
            "code": "TASK_LIMIT_REACHED",
            "message": "Limite de tarefas ativas atingido (máx. 5)"
        })

class LimiteHighAtingido(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail={
            "code": "HIGH_PRIORITY_LIMIT_REACHED",
            "message": "Limite de tarefas de alta prioridade atingido (máx. 2)"
        })

class StatusRetrocesso(HTTPException):
    def __init__(self):
        super().__init__(status_code=422, detail={
            "code": "INVALID_STATUS_TRANSITION",
            "message": "Não é permitido retroceder o status da tarefa"
        })

class DataInvalida(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail={
            "code": "INVALID_DUE_DATE",
            "message": "A data de vencimento deve ser no futuro"
        })