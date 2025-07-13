# ternary operator / condition expression
# it's a way to write if else statement in single line or expression
age=18
print("Can vote" if age>=18 else "Can't vote")


# string method
# len method
name="Manan"
print(len(name))

# find method
result=name.find("n")

# capitalize method
car="bMW"
res=car.capitalize()
print(res)

# upper method
ups="ASHA"
print(ups.upper())

# lower method
lws="MANAN"
print(lws.lower())

# isalpha method 
# return true is there's no symbol or numeric and false if there's
cars="Tata1-Nivia---"
che=cars.isalpha()
print(che)

# isdigit method
# check whether there's a numeric digit or not
checdigit=cars.isdigit()
print(checdigit)

# count method
rests=cars.count("-")
print(rests)

# replace method
print(cars.replace("-"," "))

# reverse method
reversed_Cars=cars[::-1]
print(reversed_Cars)


# quick code
# we have to create a program where we are asking user for password
# make sure password contains and follow these
# max character 12
# no space
# no digit

# password = input("Enter your password: ")

# if len(password) > 12:
#     print("Password too long! Maximum 12 characters allowed.")
# elif ' ' in password:
#     print("Password should not contain spaces.")
# elif any(char.isdigit() for char in password):
#     print("Password should not contain digits.")
# else:
#     print("Password is valid.")
    
    
# String indexing :  allow us to access any character using []
#  by this we can call start point and end point along with stop point
# syntax : [start-index:end-index-number]
# using negative value as index will start reading from RHS instead of LHS
credits="1234-4321-5432"
print(credits[0])
print(credits[0:4])
print(credits[5:9])
print(credits[-3])
word = "PYTHON"

print(word[0])  
print(word[1])  
print(word[-1])  
print(word[-2])  


# Format specifier 
# it helps us to control how a value display on output
# we can use them with format method of f-string in modern python
# common format specifier
# d    intger   {} or {:d}
# f    float    {:f}
# .2f  2-decimal place  {:0.2f}
# s    string   {:s}
# %    percentage  {:.02%}
# >    right align   {:>5}
# <    left align    {:<5}
# ^    center align  {:^5}

name = "Manan"
age = 22
height = 5.113
print("My name is {}, I am {} years old.".format(name, age))
print("My height is {:.2f} feet.".format(height))

print(f"My height is {height:.1f} feet.")

price1=3.145
price2=4.5643
price3=324.234

print(f"Price 1 is : {price1:1f}")
print(f"Price 2 is : {price1:3f}")
print(f"Price 3 is : {price1:2f}")

num = 45

print("Number is {:>5}".format(num))   
print("Number is {:<5}".format(num))   
print("Number is {:^5}".format(num))