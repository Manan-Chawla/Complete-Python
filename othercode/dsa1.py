# DATA 

# ALGO

# PSUEDOCODE

# FLOWCHART

# * means we are importing every function
from array import *    # type: ignore
# array_name=array('typecode',[values])
# i->integer
# f->float
# u->char
arr1=array('i',[1,2,3,4,5])

# index value --> start from zero
# 10---> max=0-9
# print(arr1[2])
# print(arr1[9])

# traversing a array/list/node
# printing is not refer as traversing becz we are just print the value
# not performing any opt.

# python array and cpp array
# ar=[1,2,3,4]--->cpp  it is not a dynamic
# vector---> dynamic array
# ar=[1,2,3,4]--->py


# append method
# allow add elements
# it will add element at last
arr1.append(6)

    
# insert method
arr1.insert(3,20)


# extend method
ar1=array('i',[10,20,30])
ar2=array('i',[40,40,60])
ar1.extend(ar2)

# remove method
arr1.remove(20)

# pop method---> last element remove
arr1.pop()

# reverse method
arr1.reverse()

# printing of array
for i in arr1:
    print(i)
    
for i in ar1:
    print(i)