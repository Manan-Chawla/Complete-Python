# Dictionary --> it is a collection of key values pains which are in ordered and changeable , it doesn't allow
#                duplicates.

capitals ={"usa":"washington dc",
           "India":"delhi",
           "russia":"moscow"}

# print(dir(capitals))

print(capitals.get("usa"))  # get function is used to get that element or key's value

if(capitals.get("japan")):
    print("Yes we have that in list")
else:
    print("no we dont have this")
    
capitals.update({"germany":"berlin"})  
# we can even add element using udpate and also we can update existing keys too
capitals.update({"India":"New Delhi"})
print(capitals)


capitals.pop("russia")
# this will remove russia from dictionary
print(capitals)


capitals.popitem()
# this will remove the latest key entered in the dictionary
print(capitals)


# keys function is used to return all keys within the dictionary
keys=capitals.keys()
for k in keys:
    print(k,"I am a key")
    
# values function is used to return all the values within the dictionary
values=capitals.values()
# for v in values:
#     for k in keys:
#         print("the value of ", k, " is : ", v)
#         break
#     print()

for k,v in keys , values:
    print(f"The capital of {k} is {v}")
    
# items are refer as the combination or group of key : value in dictionary
# item function is used to get the combination of key and value
items=capitals.items()
for key, value in items:
    print(f"{key} : {value}")

capitals.clear()
# this will clear out whole dictionary
print(capitals)