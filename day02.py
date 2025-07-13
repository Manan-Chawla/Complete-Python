# function
# syntax : def function_name(): print("prompt/output here")
def hello() :
    print("Hello")
hello()

a=10
b=20
# function with the arguments
def Adds(a,b):
    print("Addition : ",(a+b))
Adds(a,b)

# create a program which uses data and time along with the function
import datetime 
from datetime import datetime
now=datetime.now()
print("Date : ",now.date())

print("Welcome user enter your name to proceed for Application")
name=str(input("Enter your full name here : "  ))
print(f"Welcome {name} to the CENTRAL BANK of INDIA")
def printstime():
    print("Current time is : ",now.time())
printstime()


# by using timedelta from datetime module we can get date on day wise
# for example we can print date for 5 days
from datetime import timedelta
future=now.date()+timedelta(days=5)
#this will print the date after 5 days from now
print("5 days later : ",future)
past=now.date()-timedelta(days=5)
print("5 days previous : ",past)
    
# similarly we can even print time
future_time=now+timedelta(hours=5)
print("Future time : ",future_time)
past_time=now-timedelta(hours=5)
print("Past time : ",past_time)

# create a function which takes user's product name, price and quantity and returns 
# total
product_name=input("Enter the product name : ")
quantity=int(input("Enter the number of product you want : "))
price=100

if product_name=="Dettol":
    price+=100  #this means price of dettol is 200
elif product_name=="Brush":
    price-=20  # this means brush cost 60
else :
    price+=300  # this means other will cost 400

totalprice=quantity*price
def totals():
    print(f"The total of your bill in which you purchased {product_name} with quantity of {quantity} is : ",{totalprice})
    
totals()

