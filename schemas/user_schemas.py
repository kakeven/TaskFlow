from pydantic import BaseModel
from datetime import datetime
class User_schema(BaseModel):
    name:str
    email:str
    password:str

    class Config:
        from_attributes = True

class User_schemaResponse(BaseModel):
    name: str
    email: str
    id: int
    created_at: datetime
    class Config:
        from_attributes = True


class Login_schema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True