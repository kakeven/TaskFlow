from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,APIRouter
from schemas.user_schemas import User_schema,User_schemaResponse
from services.user_service import criar_user
from dependencies.dependency import get_session


user_router= APIRouter(prefix="/user",tags=["user"])
@user_router.post("/",response_model=User_schemaResponse)
async def criar_conta(user_schema: User_schema , session: Session = Depends(get_session) ):
    try: 
       return criar_user(user_schema,session)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))