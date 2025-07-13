# Math module
# The math module in Python 
# provides access to mathematical functions defined by the C standard. 

# it allow us to these feature
'''
access to constant math object
trigo. function
log and expo function
num. theory and representative func
'''

# to use this module we need to import it 
# import math

# we can even use this module as variable or
# name it as we want

import math as m


#  constants --->    pi and e or eular
# this will import pi from math module which calles as m
print(f"The value of PI is {m.pi}")  
print(f"The value of euler is : {m.e}")


# square root method
res=m.sqrt(81)
print("The square root of 81 is : ",res)
# power method return powered value of number
res2=m.pow(2,3)
res3=m.pow(2,2)
print("The cube of 2 is : ",res2)
print("The square of 2 is : ",res3)


# factorial function
res4=m.factorial(5)
print("The factorial of 5 is : ",res4)

# sin, cons and tan function
res5=m.sin(5)
print("The value of 5 in sin's angle is : ",res5)

res6=m.cos(6)
print("The value of 6 in cos's angle is : ",res6)

res7=m.tan(7)
print("The value of 7 in tan's angle is : ",res7)

# log method
ln_10=m.log(10)
print("The natural log of 10 is : ",ln_10)

# floor method : return largest integer less than or equal to x 
# ceil method : return the smallest integer less than or equal to x
value = 4.7
floor_value = m.floor(value)
ceil_value = m.ceil(value)

print("The floor value is : ",floor_value)
print("The ceil value is : ",ceil_value)