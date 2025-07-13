<<<<<<< HEAD
#need to create a array and then add it's element
vars=[1,2,3]
total=0
for ele in vars:
    total+=ele
    
print("Sum of element : ",total)


# array
cars=['bmw','mercs','tata','ford']
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print("now using loop")
for ele in cars:
    print(f"{ele}")


# merge two array in one
ar1=[10,20,30]
ar2=[40,50,60]
ar3=ar1+ar2
print(ar3)


#adding two array's value in one
ar3 = [x + y for x, y in zip(ar1, ar2)]  # Adds corresponding elements
print(ar3) 


# Zip method ===> it is use to combine two array or values
names=["Manan","Max","Morbius"]
ages=[24,25,39]

newlistdata=zip(names,ages)
# after zipping data we need to convert that in list or need to call list function
print(list(newlistdata))

for name, age in zip(names, ages):
  print(f"{name} is {age} years old.")


# extend method ===> to add element from another list or array
mylist1=[100,200,300]
mylist2=[300,200,100]
mylist1.extend(mylist2)
print(mylist1)

# append method ==> this is used to add a single element in list or array
newlist=['A','B','C']
newlist.append('D')
print(newlist)

# if we append a list to another list using append(), the entire list you are 
# appending will be added as a single element, creating a nested list

my_list = [1, 2, 3]
another_list = [4, 5]
my_list.append(another_list)
print(my_list) 
=======
#need to create a array and then add it's element
vars=[1,2,3]
total=0
for ele in vars:
    total+=ele
    
print("Sum of element : ",total)


# array
cars=['bmw','mercs','tata','ford']
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print("now using loop")
for ele in cars:
    print(f"{ele}")


# merge two array in one
ar1=[10,20,30]
ar2=[40,50,60]
ar3=ar1+ar2
print(ar3)


#adding two array's value in one
ar3 = [x + y for x, y in zip(ar1, ar2)]  # Adds corresponding elements
print(ar3) 


# Zip method ===> it is use to combine two array or values
names=["Manan","Max","Morbius"]
ages=[24,25,39]

newlistdata=zip(names,ages)
# after zipping data we need to convert that in list or need to call list function
print(list(newlistdata))

for name, age in zip(names, ages):
  print(f"{name} is {age} years old.")


# extend method ===> to add element from another list or array
mylist1=[100,200,300]
mylist2=[300,200,100]
mylist1.extend(mylist2)
print(mylist1)

# append method ==> this is used to add a single element in list or array
newlist=['A','B','C']
newlist.append('D')
print(newlist)

# if we append a list to another list using append(), the entire list you are 
# appending will be added as a single element, creating a nested list

my_list = [1, 2, 3]
another_list = [4, 5]
my_list.append(another_list)
print(my_list) 
>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
