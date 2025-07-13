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
school(name="Didi",section="A")