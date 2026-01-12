# FastAPI
FastAPI is a modern Python web framework, very efficient in building APIs.
FastAPI has been developed by Sebastian Ramirez in Dec. 2018. FastAPI
0.68.0 is the currently available version. The latest version requires Python
3.6 or above. It is one of the fastest web frameworks of Python.


# FastAPI –EnvironmentSetup
To install FastAPI (preferably in a virtual environment), use pip installer.
pip3 install fastapi

# Installing Uvicorn using PIP
FastAPI doesn’t come with any built-in server application. To run FastAPI
app, you need an ASGI server called uvicorn, so install the same too, using
pip installer. It will also install uvicorn’s dependencies - asgiref, click, h11,
and typing-extensions
pip3 install uvicorn


# Setting up folder
create a folder
inside folder create folder
--> mkdir fastapiproject
--> cd fastapiproject
--> python -m venv venv
--> venv\scripts\activate
--> pip install fastapi uvicorn

# Setting a new code file
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
 return {"message": "Hello World"}

# how to run -->
To run fastapi with uvicorn server write command --> python -m uvicorn main:app --reload


# to open documentation of fast api with swagger docs
write this url on browser --> http://127.0.0.1:8000/docs

FastAPI uses Swagger UI to produce this documentation. 


# Swagger Docs
* It is a Interactive UI
* Auto generated Docs


# Routing methods
GET --> fetch data
POST --> Send data
PUT --> Update Data
Delete --> Delete data


# Dynamic URLs
for ex:-
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "status": "User fetched"
    }

Now in the code above -->
user_id is autmotic validate as soon we enter a data or number in url
but if we pass a text then api will throw error



# Query based urls
In these we pass data using query or ? sign and values of data after that
for ex :-
@app.get("/search")
def search(city: str, rating: int):
    return {
        "city": city,
        "rating": rating
    }

to run this over browser we use this url -->
http://127.0.0.1:8000/search?city=Delhi&rating=5


It will show case us data in this format
{
  "city": "delhi",
  "rating": 5
}


# Schemas or Class
When we create a class which generally use in POST method, it refer as schema.
More like a object which allow us to post data into our API.
There are two ways to create schemas
1. Within same file or python :- 
Just create a class by importing BaseModel from pydantic , and use it.
2. Creating another file :-
STEPS -->
1. Create a new file named it as schemas.py
2. import --> from pydantic import BaseModel 
Ex of class -->
class Student(BaseModel):
      studentid : int
      studentname : str
Now to use it in our main file of python we need to import this class like this -->
from schemas import Student 



# POST METHOD URLS
In FastAPI, POST body = Pydantic model, is very important

--> Post method use for 
1. Send data from client to server
2. Create resources
3. Perform action like login , register etc

NOTE :  POST DATA IS SENT IN REQUEST BODY NOT URL

first we need to import it ->
from pydantic import BaseModel

Model has to be there inorder to use it, so here we will create a class-->

class User(BaseModel):
    name:str
    age:int

This is route for the model in order to use POST
@app.post("/users")
def create_user(user:User):
    return {
        "message":"User created",
        "User":user
    }


Now we need to test this using swagger docs go to url --> localhost:8000/docs
In POST/user section
write query like this -->
{
    "name":"Manan",
    "age":24
}

Then click on execute you will see Response body like this :-
{
  "message": "User created",
  "User": {
    "name": "Manan",
    "age": 24
  }
}



# Response Model -->
It defines as 
* what data will api return to client
* it hides unwanted fields
* it makes api predictable and clean
* also helps to make swagger blogs more improved

But there are some problems with response model such as :- 
*  no guarantee of response structure
* harder for frontend to handle
*  swagger not strict 

ex:- 
class StudentResponse(BaseModel):
    message:str
    student: StudentData
@app.post("/student", response_model=StudentResponse, status_code=201)
def students(student: StudentData):
    return {
        "message": "Student created successfully",
        "student": student
    }


# Creating DATAABSE CONNECTION --> 
1. install sqlalchemy --> pip install sqlalchemy 
2. create files --> db.py , models.py and schemas.py (if not exist early)
3. Now before configure our connection with database using sqlalchmey we need to understand some basic:-
** Important Library and function -->

a. create_engine 
-> it creates a connection to the database
-> it is more like to define where is my database

b. sessionmaker
-> it use to create database session
-> session is more like a conversation with database but only once
-> use because every request with database require sessions
-> it helps to avoid conflicts and data corruption

c. declarative_base
-> it is the base class of ORM Models
-> sqlalchemy need this in order to map the table

d. DATABASE_URL="value"
-> tells which database need to connect with
-> generally for local file or connection

e. Class Config :
       orm_mode=True
-> It returns orm objects
-> pydantic expects dict by default
-> it allow converstation between model
-> without this whole model will fails

f. BaseModel :
-> use for data validation
-> handles request and response data
-> accept data from user
-> sending clean data to frontend part

g. models.Base.metadata.create_all(bind=engine)
-> it creates tables automatically
-> reads models
-> executes sql
-> use in development phase 

h. db=SessionLocal()
   yield db
   db.close()
-> it opens session
-> yields to api
-> close session safely
-> it prevent memory leaks, locked db and also doesn't allow to crash the db

i. db: Session = Depends(get_db)
-> it injects db session into route
-> one session per request

4. now let's start on creating db->
A. open models.py and write following code :-
from sqlalchemy import Column, Integer, String
from db import Base

class CollegeStudent(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

B. open schemas.py and write code :- 
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

C. Open db.py and write code :- 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

D. Open main.py and write following code :- 
# Connecting database 
import models
from db import engine,SessionLocal
import schemas
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

# getting dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students",response_model=schemas.StudentRepsonse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.CollegeStudent(
        name=student.name,
        age=student.age
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Using swagger's doc for testing api
1. GET
* click on GET which is default route
* Click on Execute button
* It will show case what we passed in that function as response body with code 200

