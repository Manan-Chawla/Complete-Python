<<<<<<< HEAD
# # printing in python
# print("Hello Manan")
# print("Enter your name pal!")
# #getting input
# # name = input()
# # print("Your name is  : ",name)


# # for running our python code in vs-code
# # we use python filename.py
# # then just press enter

# print("Today", "is", "Monday")
# # sep is used to provide seperation between
# # words by providing it's value in double quotes
# # it's a inbuilt feature or function
# print("Today", "is", "Monday", sep="...")
# print("My world is ","not best",sep="---")

# # end is use to create next line or
# # we can use this to print in next line
# # end="\n" means next line we can
# # also use other methods too
# print("Today is Monday, ", end="\n")
# print("I like string beans.")


# #basic input 
# # syntax : variable = input ("prompt")
# # variable is refer to stored in memory 
# # input takes data from user
# # Prompt it's a short message which print while
# # input
# # name=input("Please enter your name")
# # print (name)

# # singer=input("whose you fav. singer")
# # print(singer)

# print("In which city you want to live ? ",end="\n")
# city="Chicago"
# print("I want to live in ",city)

# team1="BMW"
# team2="Mercs"
# print(team1,"VS",team2)



# variable
name="Manan"
age=13
percentages=98.9
canvote=True
print("String variable ",name)
print("Integer variable ",age)
print("Float variable ",percentages)
print("Boolean variable ",canvote)

# we can can variable between a prompt using curly brackets
# but for that we need to use f befor prompt in print statement
print(f"My name is {name} and i am allowed to vote is a {canvote} thing")


# this is a if statement 
if canvote :
    print("You can vote")
else :
    print("You can't vote")
    
    
# operation Arthimetic
a=10+10
b=10-10
c=10*10
d=10/10
print(a,end="\n") #addition
print(b,end="\n") #subtraction
print(c,end="\n") #multiplication
print(d,end="\n") #divison

#Typecasting : process of converting one data type into another
name="Manan"
age=24
gpa=8.9
is_student=False

type(name)
print(type(name))   #this will print it's data type
print(type(age))
print(type(gpa))
print(type(is_student))


age=float(age)  # this will convert int into float
print(age)  
print(type(age))


gpa=bool(name)
print(gpa)
print(type(gpa))




#coin flip question
import random
num = random.randint(0, 1)   
if num > 0.5:
  print('Heads')
else:
=======
# # printing in python
# print("Hello Manan")
# print("Enter your name pal!")
# #getting input
# # name = input()
# # print("Your name is  : ",name)


# # for running our python code in vs-code
# # we use python filename.py
# # then just press enter

# print("Today", "is", "Monday")
# # sep is used to provide seperation between
# # words by providing it's value in double quotes
# # it's a inbuilt feature or function
# print("Today", "is", "Monday", sep="...")
# print("My world is ","not best",sep="---")

# # end is use to create next line or
# # we can use this to print in next line
# # end="\n" means next line we can
# # also use other methods too
# print("Today is Monday, ", end="\n")
# print("I like string beans.")


# #basic input 
# # syntax : variable = input ("prompt")
# # variable is refer to stored in memory 
# # input takes data from user
# # Prompt it's a short message which print while
# # input
# # name=input("Please enter your name")
# # print (name)

# # singer=input("whose you fav. singer")
# # print(singer)

# print("In which city you want to live ? ",end="\n")
# city="Chicago"
# print("I want to live in ",city)

# team1="BMW"
# team2="Mercs"
# print(team1,"VS",team2)



# variable
name="Manan"
age=13
percentages=98.9
canvote=True
print("String variable ",name)
print("Integer variable ",age)
print("Float variable ",percentages)
print("Boolean variable ",canvote)

# we can can variable between a prompt using curly brackets
# but for that we need to use f befor prompt in print statement
print(f"My name is {name} and i am allowed to vote is a {canvote} thing")


# this is a if statement 
if canvote :
    print("You can vote")
else :
    print("You can't vote")
    
    
# operation Arthimetic
a=10+10
b=10-10
c=10*10
d=10/10
print(a,end="\n") #addition
print(b,end="\n") #subtraction
print(c,end="\n") #multiplication
print(d,end="\n") #divison

#Typecasting : process of converting one data type into another
name="Manan"
age=24
gpa=8.9
is_student=False

type(name)
print(type(name))   #this will print it's data type
print(type(age))
print(type(gpa))
print(type(is_student))


age=float(age)  # this will convert int into float
print(age)  
print(type(age))


gpa=bool(name)
print(gpa)
print(type(gpa))




#coin flip question
import random
num = random.randint(0, 1)   
if num > 0.5:
  print('Heads')
else:
>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
  print('Tails')