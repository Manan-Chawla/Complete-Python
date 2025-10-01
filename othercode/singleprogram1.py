# # Array
# # list
# # sets
# # tuple
# # dic 


# # array module

from array import * # type: ignore

# arr1=array('i',[10,20,30,40])

# # add value
# arr1.append(50)


# # insert method
# arr1.insert(0,100)

# # extend method
# arr2=array('i',[100,200,300,400,500])

# arr1.extend(arr2)

# # remove 
# arr1.remove(100)

# # pop 
# arr1.pop()

# # get element using index
# print(arr1[5])

# arr1.reverse()

# newname=array('u',['B','E','L','L','A'])
# print(newname.tolist())
# # print(newname.tostring())
# # print(arr1) we dont use this
# for ele in arr1:
#     print(ele)
    


# bella=array('i',[10,20,30,40,50,60,10,10,10,10])
# c=bella.count(10)
# print(c)



# membership operator
# in
# not in

# word="Bella"
# if "e" not in word:
#     print("Yes she is gundi bhen")
# else:
#     print("cute gundi")


# list comprehension
# arr1=[10,20,30,40,50]
# ar1=[10,20,30]
# ar1=[x**2 for x in ar1]
# print(ar1)


list1=[1,2,3,4]
list1=[x*2 for x in list1]
print(list1)
