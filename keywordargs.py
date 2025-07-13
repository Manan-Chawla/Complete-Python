<<<<<<< HEAD
# default keyword arguments
def greets(name,message="Welcome to the Jurrasic park"):
    print(f"{message}, {name}")
greets(name="Noor")


# Arbitary keyword arguments
def hello(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
hello(name="Bella",age=19,country="US")


# standar keyword arguments
def school(name,section):
    print(f"{name} is in section {section}")
=======
# default keyword arguments
def greets(name,message="Welcome to the Jurrasic park"):
    print(f"{message}, {name}")
greets(name="Noor")


# Arbitary keyword arguments
def hello(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
hello(name="Bella",age=19,country="US")


# standar keyword arguments
def school(name,section):
    print(f"{name} is in section {section}")
>>>>>>> f124a1fcc03fb8662e4e7786201ec0d2cecb7478
school(name="Didi",section="A")