"""
Abstract Classes and Methods in Python:-
    
    In Python, abstract classes and abstract methods are a part of the abc (Abstract Base Class) module, which provides a way
    to define blueprints for other classes.
    
"""

"""
Abstract Class:-

    Definition: A class is considered abstract if it contains one or more abstract methods.
    Purpose: Abstract classes serve as templates for other classes. They enforce certain methods to be implemented in derived classes.
    Implementation: Abstract classes are created using the ABC (Abstract Base Class) from the abc module.
    Instantiation: Abstract classes cannot be instantiated directly.
    
    
Abstract Method:-

    Definition: A method declared in an abstract class with the @abstractmethod decorator but without any implementation.
    Purpose: Abstract methods act as placeholders for methods that must be implemented in subclasses.
    Implementation: Subclasses that inherit the abstract class must provide an implementation for all abstract methods.
"""    

from abc import ABC, abstractmethod

class Shape(ABC):
    # Abstract method
    @abstractmethod
    def area(self):
        pass

    # Abstract method
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing abstract methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate Shape (abstract class)
# s = Shape()  # Raises TypeError

# Instantiating Rectangle (concrete class)
r = Rectangle(10, 5)
print(f"Area: {r.area()}")  # Output: Area: 50
print(f"Perimeter: {r.perimeter()}")  # Output: Perimeter: 30


"""
Benefits of Abstract Classes:-
    Enforcing Design: Ensures that derived classes implement specific methods, promoting consistency.
    Polymorphism: Abstract classes enable polymorphic behavior where different subclasses implement the abstract methods differently.
"""