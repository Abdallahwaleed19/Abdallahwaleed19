

"""
    Method Overriding in Python:-
    
	-The overridden method in the subclass must have the same name, parameters, and return type as the method in the superclass.

	-In Python, method overriding allows the subclass to change or extend the behavior of the parent class’s methods.
"""


# Python program to demonstrate 
# method overriding (change behavior)


class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    

# Example usage
p = Parent()
p.greet()  # Output: Hello from Parent!

c = Child()
c.greet()  # Output: Hello from Child!


# Python program to demonstrate 
# method overriding (extend behavior)

# If the subclass needs to include the behavior of the parent class while adding new functionality, it can use the super() function.

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Call the parent class's 'greet' method
        print("Hello from Child!")

# Example usage
c = Child()
c.greet()
# Output:
# Hello from Parent!
# Hello from Child!



"""
Overriding Special Methods (Magic Functions):-
Python allows overriding special (magic) methods to customize the behavior of built-in operations. For example:

__str__: For string representation.
__eq__: For equality checks.
__add__: For addition.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # Overriding the string representation
        return f"{self.name}, Age: {self.age}"

p = Person("Alice", 30)
print(p)  # Output: Alice, Age: 30
