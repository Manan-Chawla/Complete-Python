# intro to class

# Classes --> contains function and attributes or variables

# we use class keyword

# regular / instance (self function)  {Public}
# class function {Private method}    @classmethod
# static functions {utility functions}  @staticmethod 
# which can use self ---> regular and class

class Students(object):
    Csec="A"
    
    # init method :-- initlializer method (we can't call it )
    def __init__(self,name):
        self.name=name
        
    # str method :-- it will help us to print the value within init method
    def __str__(self):
        return self.name
    
    def recalls(self,renamed):
        self.name=renamed
        print("My name is now ",format(self.name))



def funs():
    print("hello")

# syntax : object_name=class_name(parameter)
kelly=Students("Amy")  #parameter
print(f"She is in Section {kelly.Csec}")
print("Her name is ,",kelly.__str__())
kelly.recalls("Matlida")  # regular function ( user defined function )




# regular function 
class voter:      #class class_name:
    def __init__(self,name,age):   # constructor 
        self.name=name  # self is a attribute and help to access value or arguments
        self.age=age
    
    def tells(self):    # instance method  { regular function }
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

v1=voter("Sam",20)   # key = classname(parameter)
v1.tells()  # key.classmethod()



# class function
class college:
    c_name="MITS"
    c_sec="A"
    @classmethod
    def mycname(cls):
        print(f"My college name is {cls.c_name}")
        print(f"My section is {cls.c_sec}")

college.mycname()


# static function
class stu:
    @staticmethod
    def grade(marks):
        return marks>=40 
print(stu.grade(20))


class bank:
    def __init__(self):   # Access sepecifier
        self._balance=1000   # one underscore --> protected
        self.__pin=1234      # two underscore --> private
        
b1=bank()
print(b1._balance)
# print(b1.__pin)


class animal:
    def lion(self):
        print("Lion is the king of jungle")

class fish(animal):
    def shark(self):
        print("Shark are not native to india")
    
f1=fish()
f1.lion()
f1.shark()  
   
# polymorphism 
class earth1:
    def earth(self):
        print("True earth1 in first")
    
class earth2:
    def earth(self):
        print("True earth2 in second")


for animals in (earth1(),earth2()):
    animals.earth()