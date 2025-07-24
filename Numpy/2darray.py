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