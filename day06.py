# # for loop 
# for x in range(1,11):
#     print("The value is : ",x)
    
# # nested loop or condition :
# for x in range(1,6):
#     if x==2:
#         print("You got the power")
#         break
#     else:
#         print("You got nothing pal")
        
        

# Collection : single 'variable' used to store multiple values are collection
# It has three types
# List = [] are ordered and changeable and allow duplicates values
# Set = {} are unordered and immutable but can add or remove values and 
#       not allow duplicates
# Tuple = () are ordered and unchangeable but allow to store duplicate and much
#         faster

car=["merc","bmw","tata"]





# list operation
print(car)
car.append("ford")   # adding element
print(car.count("bmw")) # count the number of element which are same 
car[0]="Ferrari"   # updating value
car.insert(3,"Peterbuilt")  # adding value at specific 
newcars=["Peugot","Tesla"]  #new list
car.extend(newcars)   # extending or adding two list 
car.remove("bmw") # removing element from list
removed_item=car.pop(2)  # it will remove that item from list using index no.

car.clear()  # clear all the element from the list
for x in car:
    print(x)


# set
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set_with_duplicates = {1, 2, 2, 3, 3, 3} # set with duplicates values
print(my_set_with_duplicates) # but this will return only one of each duplicate value

# union operation
set1={1,2,3}
set2={4,5,6}
new_set=set1 | set2  # this will add both set or we can even use union method too
union_sets= set1.union(set2)  # using union method
print(new_set)
print(union_sets)

# intersection method
# finds element present in both sets
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
print(set3 & set4) # we can use ampersand for this 
print(set3.intersection(set4))  # we can also use intersection method 


# difference method
# return element in first set but not in second
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}
print(set5 - set6) # we can use - operator
print(set5.difference(set6))  # and also difference method too

# tuple
games=("Cricket","polo","hockey")
print(games)
