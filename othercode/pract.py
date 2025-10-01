# # sum of number
# n=int(input("enter number : "))
# sum=0
# for s in range(1,n):
#     sum=s+sum
# print("The sum is : ",sum)




# random number 
# import random as r
# num=input("enter a number between 1 to 10 : ")
# rs=r.randint(1,10)
# if rs==num:
#     print("Match")
# else:
#     print("Not matched")


# getting square of number
# import math as m
# num1=int(input("enter a number : "))
# sq=m.pow(num1,2)
# squ=int(sq)
# print(f"The square of {num1} is {squ}")



# reverse name
# name=str(input("Enter your name  : "))
# newname=name[::-1]
# print(f"The Reverse of {name} is : ",newname)



# extending two list
# car=["ford","tata","suzuki","mazda","bmw"]
# for c in car:
#     print("Name of car brand is : ",c)
    
# car2=["toyota","shelby","rolls royce","audi"]
# car.extend(car2)

# for a in car:
#     print(a)



# operation on array's value
# have to reduced price by 5 in each element
appleprice=[10,20,30,40,50]
for aps in appleprice:
    newprice=aps-5
    print(newprice)

# for aps in appleprice:
#     custromprice=aps[3]-10

# print(custromprice)