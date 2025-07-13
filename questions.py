# get sum of two variable 
# num1=int(input("enter number1 : "))
# num2=int(input("enter number2 : "))
# num3=num1+num2
# print(num3)



# # print hello world
# print("hello world")




# to provide square root of a number
# first method
# nums=int(input("enter a numbere here : "))
# sr=nums**(1/2)
# print("Square root of given number is  : ",sr)
# # second method
# import math
# numbers=int(input("enter a number here "))
# srs=math.sqrt(numbers)
# print("Square root of given number is  : ",srs)



# calulate the area of triangle
# base=10
# height=14
# area=(base*height)/2
# print(f"Area of triangle : {area}")



# swap two variable
# first method
# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(f"Updated value of a : {a}")
# print(f"Updated value of b : {b}")
# # second method
# x=100
# y=200
# x,y=y,x
# print(f"Updated value of x : {x}")
# print(f"Updated value of y : {y}")




# conversion program
# km=1
# miles=0.621371
# distance=float(input("enter distance you want to convert : "))
# unit=str(input("enter k for km and m for miles : "))
# if unit=='k':
#     distance *=km
#     print("Distance in km is : ",distance)
# elif unit=='m':
#     distance *=miles
#     print("Distance in miles : ",distance)
# else :
#     print("wrong option choose")
    



# to check whether user's input is a +ve , -ve or neutral digit
# num=float(input("enter a number : "))
# if num>0:
#     print("Positive number ")
# elif num<0:
#     print("Negative number ")
# elif num==0:
#     print("Neutal number")
# else:
#     print("Please enter a number only")


# to check whether number is odd or even
# num=float(input("enter a number : "))
# if num%2==0:
#     print("Even number")
# elif num%2!=0:
#     print("Odd number")
# else:
#     print("Enter a number properly")


# to check a year is leap or not
# year=int(input("enter a year : "))
# if(year%400==0) and (year%100==0):
#     print(f"{year} is a leap year")
# elif (year%4==0) and (year%100!=0):
#     print(f"{year} is a leap year")
# else :
#     print("Year is not a leap year")




# check which number is greater between three
# a=10
# b=20
# c=15
# if a>b and a>c:
#     print("A is greater than B and C")
# elif b>a or b>c :
#     print("B is greater than C and A")
# else:
#     print("C is greater than A and B")



# program to check whether number is prime or not
# a=int(input("Enter number to check  : "))
# if a==1:
#     print("It is a not a prime number ")
# if a>1:
#     for i in range(2,a):
#      if a%i==0:
#         print("it is not a prime number")
#         break
#     else:
#         print("It is a prime number")



# create a program to genrate random number
# import random 
# a= random.randint(0,100)
# usernum=int(input("Enter your number to guess whether you are lucky or not : "))
# if usernum==a:
#     print("you are lucky pal")
# else:
#     print("Sorry better luck next time")
# print(f"Number was {a}")
        