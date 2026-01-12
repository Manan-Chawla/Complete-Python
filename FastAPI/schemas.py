from pydantic import BaseModel  
class PostCreate(BaseModel):
    title:str
    content:str
    
    
class StudentCreate(BaseModel):
    name:str
    age:int

class StudentRepsonse(BaseModel):
    id:int
    name:str
    age:int
    
    class Config:
        orm_mode=True 