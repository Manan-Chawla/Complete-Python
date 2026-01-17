# from pydantic import BaseModel  
# class PostCreate(BaseModel):
#     title:str
#     content:str
    
# # for put method
# class StudentBase(BaseModel):
#     name: str
#     age: int


    
# class StudentCreate(BaseModel):
#     name:str
#     age:int


# class StudentResponse(BaseModel):   # ✅ correct spelling
#     id: int
#     name: str
#     age: int

#     class Config:
#         orm_mode = True 

from pydantic import BaseModel  

class PostCreate(BaseModel):
    title: str
    content: str


class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True



# for JWT tokens 
class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
