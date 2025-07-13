# asking user to enter num1 and num2
num1=int(input("enter value of num1  : "))
num2=int(input("enter value of num2  : "))

# asking user for operation type
operator=input("enter an operator {+,-,*,/,%} : ")
if operator =="+":
    result=num1+num2
    print(result)
elif operator =="-":
    result=num1-num2
    print(result)
elif operator =="*":
    result=num1*num2
    print(result)
elif operator =="/":
    result=num1/num2
    print(result)
elif operator =="%":
    result=num1%num2
    print(result)
else :
    print("wrong operator entered")
    