# FastAPI

FastAPI is a modern Python web framework, very efficient in building APIs.
FastAPI has been developed by Sebastian Ramirez in Dec. 2018.
FastAPI 0.68.0 is the currently available version.
The latest version requires Python 3.6 or above.
It is one of the fastest web frameworks of Python.

---

## FastAPI – Environment Setup

To install FastAPI (preferably in a virtual environment), use pip installer.

```bash
pip3 install fastapi
```

---

## Installing Uvicorn using PIP

FastAPI doesn’t come with any built-in server application.
To run FastAPI app, you need an ASGI server called uvicorn, so install the same too, using pip installer.

It will also install uvicorn’s dependencies:

* asgiref
* click
* h11
* typing-extensions

```bash
pip3 install uvicorn
```

---

## Setting up Folder

Create a folder and setup virtual environment.

```bash
mkdir fastapiproject
cd fastapiproject
python -m venv venv
venv\scripts\activate
pip install fastapi uvicorn
```

---

## Setting a New Code File

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}
```

---

## How to Run FastAPI

To run fastapi with uvicorn server write command:

```bash
python -m uvicorn main:app --reload
```

---

## Swagger Documentation

To open documentation of fast api with swagger docs
write this url on browser:

```
http://127.0.0.1:8000/docs
```

FastAPI uses Swagger UI to produce this documentation.

---

## Swagger Docs

* It is a Interactive UI
* Auto generated Docs

---

## Routing Methods

* **GET** → fetch data
* **POST** → Send data
* **PUT** → Update Data
* **DELETE** → Delete data

---

## Dynamic URLs

For example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "status": "User fetched"
    }
```

Now in the code above →

user_id is automatic validate as soon we enter a data or number in url
but if we pass a text then api will throw error

---

## Query Based URLs

In these we pass data using query or `?` sign and values of data after that.

For example:

```python
@app.get("/search")
def search(city: str, rating: int):
    return {
        "city": city,
        "rating": rating
    }
```

To run this over browser we use this url →

```
http://127.0.0.1:8000/search?city=Delhi&rating=5
```

It will show case us data in this format:

```json
{
  "city": "delhi",
  "rating": 5
}
```

---

## POST Method URLs

In FastAPI, POST body = Pydantic model, is very important.

### Post method use for

1. Send data from client to server
2. Create resources
3. Perform action like login, register etc

**NOTE:** POST DATA IS SENT IN REQUEST BODY NOT URL

First we need to import it →

```python
from pydantic import BaseModel
```

Model has to be there inorder to use it, so here we will create a class →

```python
class User(BaseModel):
    name: str
    age: int
```

This is route for the model in order to use POST:

```python
@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "User": user
    }
```

---

## Testing POST using Swagger Docs

Go to url →

```
http://localhost:8000/docs
```

In POST /user section
write query like this →

```json
{
    "name": "Manan",
    "age": 24
}
```

Then click on Execute, you will see Response body like this:

```json
{
  "message": "User created",
  "User": {
    "name": "Manan",
    "age": 24
  }
}
```

---

## Using Swagger Docs for Testing API

### GET

* Click on GET which is default route
* Click on Execute button
* It will show case what we passed in that function as response body with code 200





## Passing an html page in FastAPI
1. first we need to create a 'template' folder within our main folder
2. Create a 'imdex.html' file within
3. write down following code :-
   ```
<html>
<head>
    <title>Item Detail</title>
</head>
<body>
    <h1>Item ID: {{ id }}</h1>
    <p>Rendered via Jinja2!</p>
</body>
</html>
   ```
4. Now import following packages in our main.py
**from fastapi.templating import Jinja2Templates**, 
**from fastapi.responses import HTMLResponse**, 
**from fastapi import Request**
5. Now write down the route or url for it
```
# jinja templates
templates=Jinja2Templates(directory="templates")
```
@app.get("/i/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )
```
6. Now to run this on browser use this :-
```
http://localhost:8000/i/1
```
