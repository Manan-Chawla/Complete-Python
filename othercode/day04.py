<<<<<<< HEAD
# logical operator = use to evaluate multiple condition
# or = at least one condition has to be true
# and = both condition must be true
# not = inverts the condition (not false , not true)


name=str(input("enter your name : "))
age=int(input("enter your age : "))

if name=="manan" and age==24:
    print("You can enter ") 
elif name=="max" or age==22:
    print("we have to think about this")
elif name=="amy" and not age==24:
    print("Sure you can but we have to see some id ")
else :
=======
# logical operator = use to evaluate multiple condition
# or = at least one condition has to be true
# and = both condition must be true
# not = inverts the condition (not false , not true)


name=str(input("enter your name : "))
age=int(input("enter your age : "))

if name=="manan" and age==24:
    print("You can enter ") 
elif name=="max" or age==22:
    print("we have to think about this")
elif name=="amy" and not age==24:
    print("Sure you can but we have to see some id ")
else :
>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
    print("You can't enter ")