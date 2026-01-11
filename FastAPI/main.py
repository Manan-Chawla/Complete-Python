from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field 

app=FastAPI()

@app.get("/")
def root():
    return "hi"

@app.get("/about")
def about():
    return {"name": "Manan", "learning": "FastAPI"}



# dynamic url
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "status": "User fetched"
    }

# query parameter based url
@app.get("/search")
def search(city: str, rating: int):
    return {
        "city": city,
        "rating": rating
    }


# test1 url
@app.get("/hello/{name}")
def hello(name):
    return f"Hello,{name}"


#test2 url
@app.get("/filter")
def filter(min_price:int,max_price:int):
    return{
        "minprice":min_price,
        "maxprice":max_price
    }

# POST URLS

# model
class User(BaseModel):
    name:str
    age:int


@app.post("/users")
def create_user(user:User):
    return {
        "message":"User created",
        "User":user
    }



# test1 post url
class Login(BaseModel):
    email:str
    password:str


@app.post("/login")
def login_user(user: Login):
    return {
        "message": "Login successful",
        "email": user.email
    }



class Order(BaseModel):
    quantity: int 
    status: str

@app.post("/order")
def place_order(order:Order):
    if order.quantity <10:
        return{
            "error":"sorry we can't take low orders"
        }
    return{
        "message":"Order placed"
    }

class StudentData(BaseModel):
    student_id: int = Field(..., gt=0)
    student_name: str = Field(..., min_length=3)
    student_age: int = Field(..., gt=3, lt=100)

@app.post("/student")
def students(student: StudentData):
    return {
        "message": "Student data received successfully",
        "data": {
            "student_id": student.student_id,
            "student_name": student.student_name,
            "student_age": student.student_age
        }
    }


# response model 
class StudentResponse(BaseModel):
    message:str
    student: StudentData
@app.post("/student", response_model=StudentResponse, status_code=201)
def students(student: StudentData):
    return {
        "message": "Student created successfully",
        "student": student
    }



# blog app
text_posts = {
    1: {
        "title": "Transformer",
        "Content": "Best Movie from 2009"
    },
    2: {
        "title": "Top 5 Sci-Fi Films of the Decade",
        "Content": "A look back at the cinematic achievements that defined the 2020s (so far)."
    },
    3: {
        "title": "Review: The New Animated Series Everyone is Talking About",
        "Content": "Does it live up to the hype? A spoiler-free deep dive into the show's first season."
    },
    4: {
        "title": "Why Practical Effects Still Matter",
        "Content": "Discussing the tangible magic of prosthetics and miniatures over modern CGI."
    },
    5: {
        "title": "Underrated Horror Gems for a Cozy Night",
        "Content": "Forget the blockbusters—these lesser-known films will genuinely creep you out."
    },
    6: {
        "title": "The Evolution of Superhero Movie Soundtracks",
        "Content": "How music transforms epic battles: from sweeping orchestras to modern synth."
    },
    7: {
        "title": "My 5 Favorite AI Tools for Writers in 2026",
        "Content": "Speed up your drafting and research with these game-changing apps."
    },
    8: {
        "title": "Deep Dive: Understanding Quantum Computing Basics",
        "Content": "A simplified explanation of qubits, superposition, and what this tech means for the future."
    },
    9: {
        "title": "The 3-Step Morning Routine That Boosted My Focus",
        "Content": "Tips on leveraging the first hour of your day for maximum productivity."
    },
    10: {
        "title": "Budget Travel: How to See Europe for Under $100 a Day",
        "Content": "Insider tips on cheap flights, hostel hacks, and street food recommendations."
    },
    11: {
        "title": "Reviewing the Best Noise-Cancelling Headphones for Long Flights",
        "Content": "Which pair truly delivers quiet comfort at 30,000 feet?"
    },
    12: {
        "title": "Beginner's Guide to Sourdough: Starter Secrets",
        "Content": "Everything you need to know to maintain a healthy, bubbly starter."
    },
    13: {
        "title": "One-Pot Wonders: A Recipe for Spicy Peanut Noodles",
        "Content": "Quick, easy, and minimal cleanup for busy weeknights."
    },
    14: {
        "title": "The Power of 'No': Setting Healthy Boundaries",
        "Content": "Why saying no is often the most productive thing you can do for yourself."
    }
}

@app.get("/posts")
def get_post():
    return text_posts


@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404,details="Post not found")
    return text_posts.get(id)