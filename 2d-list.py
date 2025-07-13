# 2-d list
#  when we store list within a variable in form of list element
#  it refer as 2d list

firstaplha=["a","b","c"]
secondalpha=["d","e","f"]
thirdalpha=["g","h","i"]

# this is a 2d list as it store other list as a element
# we can access list seperatly by using index value

allaplha=[firstaplha,secondalpha,thirdalpha]
print(allaplha)

print(f"the list at 0 index is  : {allaplha[0]}")
print(f"the list at 1 index is  : {allaplha[1]}")
print(f"the list at 2 index is  : {allaplha[2]}")

for ast in allaplha:
    print(ast)  # printing all elements
    
# we can even access element within the element of a list
print(allaplha[0][1],end="______\n")  # this will access 1st element of 1st list

for collection in allaplha:
    for newalpha in collection:
        print(newalpha)  # this will print every element in list or 2d list
        
        
        
#  just like 2d list we can also create 2d tuple and 2d set
#  tuple are faster than list in context to operation


# 2d tuple
num_pad=((1,2,3),
         (4,5,6),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
    
    
# 2d sets
# for creating 2d set we need to store in list
cars_name = [{"ford", "tata", "jeep"},
             {"bmw", "mercs", "ferrari"},
             {"toyota", "honda", "suzuki"}]

for rws in cars_name:
    for rwel in rws:
        print(rwel," ")
    print()