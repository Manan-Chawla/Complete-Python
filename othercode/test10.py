
# dictionary 
# { key: value}   pair


car_comps={
    "ford":"aspire",    # single element
    "nissan":"GTr",
    "tata":"altroz",
    "kia":"seltos"
}

print(dir(car_comps))

# print(car_comps)

# for loop 
# print kerna hai using a for loop 

# keys is used to fetch all the keys
keys=car_comps.keys()
# values is used to fetch all the values
values=car_comps.values()


# items create a collection of group of keys and values
items=car_comps.items() 
# items is collection of keys and values

for keys,values in items:
    print(f"value of {keys} : {values}")

# for k in keys:
#     for v in values:
#         print(f"The value of {k} : {v}")
#         break
#     print()
    

