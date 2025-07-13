# Function : a block of reusable code , for creating this we use def keyword with ()

def hello():
    print("Hi i am good")
    
#  this is called as calling a function to perform that task for which we create it
hello()

# we can even pass parameter with a function
# remember the position of parameter does matter
def greets(age,name):
    print(f"Happy bday to {name}")
    print(f"You are now {age} years old")
    print("Wish you a very happy life")

greets(12,"Manan")


# we can return values too using function
def sums(a,b):
    c=a+b
    return c

ans=sums(10,20)
print(ans)

def display_invoice(username,amount,due_date):
    print(f"USERNAME : {username}")
    print(f"Bill Amount : {amount}")
    print(f"The due amount of ${amount} for {username} 's due date is : {due_date}")
    
display_invoice("Manan",24000,"12/10/10")