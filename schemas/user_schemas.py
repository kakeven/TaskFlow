from pydantic import BaseModel

class User_schema(BaseModel):
    name:str
    email:str
    password:str

    class Config:
        from_attributes = True