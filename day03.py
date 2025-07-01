# if statement = do some code if the condition is true else do something else

age=int(input("enter your age"))
if age>=18:
    print("you can vote")
else :
    print("you can't vote")
    
if age==20 : print("good") 
else : print("not good ")


# = use to assign
# == use to compare values
# === use to clarify that this is the only value it accept

# if elif = it just add another condition with if conditon
marks=int(input("enter your marks"))
if marks>=90:
    print("outstanding")
elif marks>=50:
    print("nice")
elif marks<34:
    print("failed")
else:
    print("you passed")
    
# nested if = when a if contains a if
if age>22:
    if age==25:
        print("you can be the winner")
else:
    print("not yet pal")   
    
# if with bool values
online=True
if online:
    print("You were there my pal")
else:
    print("You were not the guy we looking for")