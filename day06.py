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
# Tuples are in ordered manner
# they are immutable
# it refer as the collection of differ. data types

# empty tuple
emps_tuples=()
print(emps_tuples)

# mixed value tuples
mixed_tuples=(10,"Good",34.23,[1,2])
print(mixed_tuples)

# tuple without parentheses
another_tuple = 1, 2, 3
print(f"Tuple without parentheses: {another_tuple}")

# operation on tuples
my_tuple = ("a", "b", "c", "d", "e", "f")

# Accessing by index
print(f"First element: {my_tuple[0]}")
print(f"Third element: {my_tuple[2]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Second to last element: {my_tuple[-2]}")

# Slicing
print(f"Elements from index 1 to 3 (exclusive): {my_tuple[1:4]}")
print(f"Elements from the beginning to index 3 (exclusive): {my_tuple[:3]}")
print(f"Elements from index 3 to the end: {my_tuple[3:]}")
print(f"All elements (copy): {my_tuple[:]}")
print(f"Every second element: {my_tuple[::2]}")
print(f"Reverse tuple: {my_tuple[::-1]}")

# concatenation 
tupl1=(1,2,3)
tupl2=(4,5,6)
comb_tupl=tupl1+tupl2
print(comb_tupl)

# length of tuple
lens=print(len(comb_tupl))

# membership in tuple (in or not)
# check whether element is present or not
fruits = ("apple", "banana", "cherry")

print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")


# iteration in tuple
colors = ("red", "green", "blue")
print("Iterating through colors:")
for color in colors:
    print(color)
    
# unpacking tuple
# unpack the elements of a tuple into individual variables
coordinates = (10, 20)
x, y = coordinates
print(f"X coordinate: {x}, Y coordinate: {y}")

# nested tuple
# when a tuple is inside a tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested_tuple}")