# array in python
import array as ar

ar1=ar.array('i',[1,2,3,4,5])

print(ar1[3])

ar1[0]=10

if ar1[0]==10:
    print("Element is updated ")

print(ar1)


ar2=ar.array('i',[100,200,300,400,500])

ar3=ar1+ar2

print(ar3)