# polymorphism
# when there are two function with same 
# but provide differ functionalities

class one:
    def poly1(self):
        print("I am function1")

class two:
    def poly1(self):
        print("I am function2")

o1=one()
o1.poly1()

# if u follow the same pace as rn-->
# within a year u will be same as me
# i'll make sure this

# fc is object for both classes
for fc in(one(),two()):
    fc.poly1()
    
