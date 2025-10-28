# items list
food=[]

price=[]


for k in food,price:
    print(k,sep="---")
    
def funs():
    foods=input("enter food you want to get ")
    food.append(foods)
    prices=float(input("enter price for your product or food "))
    price.append(prices)

# funs()
# for i in range(len(food)):
#     print(f"{food[i]}: ${price[i]:.2f}")



from array import *

ar1=array('i',[10,20,30,40,50])

for i in ar1:
    print(f"Array value {i}")
    
    
ar1.append(60)

print(ar1[0])

choic1=input("Which operation u want to perform : remove / append / prints ")
if choic1=="remove":
    rems=int(input("enter number from list or value from list to remove "))
    ar1.remove(rems)
    print(f"{rems} is removed from list")
elif choic1=="append":
    ads=int(input("enter number you want to add in the array : "))
    ar1.append(ads)
elif choic1=="prints":
    print(ar1)
else:
    print("wrong choice entered")
    
    
def find_max_min(ar1):
    if not ar1:
        return None, None

    max_val = ar1[0]
    min_val = ar1[0]

    for element in ar1:
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element
    return max_val, min_val

rests=find_max_min(ar1)
print(rests)