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
