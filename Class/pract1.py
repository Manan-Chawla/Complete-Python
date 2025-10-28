# we have to create a class which takes input {name,roll,age}
# and display student infomation

# parental class
class bhu:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        # instance 
    def student_detail(self):
        print(f"Student name : {self.name}")
        print(f"Student roll no. : {self.roll}")
        print(f"Student age : {self.age}")    
# c1=bhu("Max",24,99)
# c1.student_detail()

# child class
class pbhu:
    def __init__(self,pname,mname):
        self.pname=pname
        self.mname=mname
        
    def parent_detail(self):
        print(f"Father's name : {self.pname}")
        print(f"Mother's name : {self.mname}")
# p1=pbhu("Sam","Erin")
# p1.parent_detail()

# now create a class to add both classes
class details(bhu,pbhu):
    def __init__(self, name, age, roll, pname, mname):
        bhu.__init__(self, name, age, roll)
        pbhu.__init__(self, pname, mname)
    
    def display_all_details(self):
        print("\n--- Student and Parent Details ---")
        self.student_detail()
        self.parent_detail()

full_info = details("Max", 24, 99, "Sam", "Erin")
full_info.display_all_details()
