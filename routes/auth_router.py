from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def autenticar():
    return {"adwd"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str ,senha:str ):
    pass