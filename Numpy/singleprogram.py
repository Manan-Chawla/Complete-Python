
# default keyword arguments
def greets(name,message="Welcome to the Jurrasic park"):
    print(f"{message}, {name}")
greets(name="Noor")


# Arbitary keyword arguments
def hello(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
hello(name="Bella",age=19,country="US")


# standar keyword arguments
def school(name,section):
    print(f"{name} is in section {section}")
school(name="Didi",section="A")


appleprice=[10,20,30,40,50]
for aps in appleprice:
    newprice=aps-5
    print(newprice)

for aps in appleprice:
    custromprice=aps[3]-10

print(custromprice)


# array
# array is collection of homogenous data strucutre or element

from array import * # type: ignore

# syntax : arr_name=array(typecode,[initalizer])
my_arr = array('i',[1,2,3,4])

# adding element in last
my_arr.append(5)


# adding element using index
my_arr.insert(0,0)

# extending a array using another array
my_extnd_array = array('i', [7,8,9,10])
my_arr.extend(my_extnd_array)


# remove
my_arr.remove(0)



for ele in my_arr:
 print(ele)



menu = {
    "A": "$4.50",
    "B": "$5.69",
    "C": "$34.90",
    "D": "$1.89",
    "E": "$2.46"
}

cart = []
total = 0.0

print("------MENU--------")
for key, value in menu.items():
    print(f"{key:5} : {value}")
print("------------------")

while True:
    food = input("Select an item or 'q' to quit: ").upper()
    if food == 'Q':
        break
    elif food in menu:
        cart.append(food)
        price = float(menu[food].replace("$", ""))
        total += price
    else:
        print("Invalid item. Please choose from the menu.")

print("\nItems in your cart:")
for item in cart:
    print(f"{item} - {menu[item]}")

print(f"Total: ${total:.2f}")




import numpy as np
a1=np.array([
    [1,2],
    [4,5] 
])

a2=np.array([
    [4,5],
    [1,2]
])

for a,b in a1,a2:
    print(a+b)
print("-------------") 
for a,b in a1,a2:
    print(a-b)
print("-------------") 
for a,b in a1,a2:
    print(a/b)
print("-------------")  
for a,b in a1,a2:
    print(a*b)
    
print("-------------") 
print(a1.size)
print(a1.ndim)
print(a1.shape)
print(a1.dtype)

print("-------------") 
print(a1[0])
print("-------------") 
print(a1[0][1])
print("-------------") 
print(a1[1,1])

print("-------------") 
print(a1[:,1])
print(a1[1,:1])
print(a1[0:2,0:2])

print("-------------") 
print(a1@a2)
print("-------------") 
print(np.dot(a1,a2))

for a,b in a1,a2:
    print(a,b.T)
    
    
    
    
    
# # array
# from array import array # type: ignore
# arr1=array('i',[1,2,3])
# arr2=array('i',[4,5,6])
# # for n in arr1,arr2:
# #     arr3=arr1[n]+arr2[n]
# #     print(arr3)
    
# add = [x + y for x, y in zip(arr1, arr2)]
# for ele in add:
#     print("Addition value is : ",ele)
# print("----------------------------------")
# # Subtract
# sub = [x - y for x, y in zip(arr1, arr2)]
# for ele in sub:
#     print("Subtraction value is : ",ele)
# print("----------------------------------")   
# # Multiply
# mul = [x * y for x, y in zip(arr1, arr2)]
# for ele in mul:
#     print("Multiplication value is : ",ele)
# print("----------------------------------")  
# # Divide
# div = [x / y for x, y in zip(arr1, arr2)]
# for ele in div:
#     print("Divide value is : ",ele)
# print("----------------------------------")


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0])      # [1, 2, 3] (1st row)
# print(matrix[0][1])   # 2        (1st row, 2nd column)

# for row in matrix:
#     print(row)

# for row in matrix:
#     for item in row:
#         print(item, end=' ')


# Matrix and it's operation
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]


add = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]

print(add)
# Output: [[6, 8], [10, 12]]

sub = [
    [A[i][j] - B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]

print(sub)

def multiply_matrices(A, B):
    result = [
        [0 for _ in range(len(B[0]))] for _ in range(len(A))
    ]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(multiply_matrices(A, B))
# Output: [[19, 22], [43, 50]]
