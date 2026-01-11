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


# Using swagger's doc for testing api
1. GET
* click on GET which is default route
* Click on Execute button
* It will show case what we passed in that function as response body with code 200

