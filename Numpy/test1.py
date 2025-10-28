# class--> collection of method and data member
# object --> instance of class
# object allow us to use class and its function

# {GIFT}

# we dont have to share everything with everyone except (babulal)
# we dont have to make someone priority always
# be with those who wants to be with u too 


class student:
    def __init__(self,name,age):
        self.name  = name
        self.age   = age
    def prints(self):
        print(self.name)
        print(self.age)
    
st1=student("didi",29)
st1.prints()