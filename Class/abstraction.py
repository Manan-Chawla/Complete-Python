from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass 

    def describe(self): 
        return "This is a geometric shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)

print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
print(circle.describe())
