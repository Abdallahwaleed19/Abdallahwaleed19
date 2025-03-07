# What is Polymorphism?

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
# with the same name that can be executed on different objects or classes.


# Example 1: Polymorphism in addition operator (operator overloading)

# num1 = 1
# num2 = 2
# print(num1+num2)

# str1 = "Python"
# str2 = "Programming"
# print(str1+" "+str2)




# Function Polymorphism in Python (Example : len() function)

# print(len("Programiz"))
# print(len(["Python", "Java", "C"]))
# print(len({"Name": "John", "Address": "Nepal"}))




# Class Polymorphism in Python

# We can use the concept of polymorphism while creating class methods as Python allows different classes to
# have methods with the same name.

# We can then later generalize calling these methods by disregarding the object we are working with. Let's 
# look at an example:

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()




# Polymorphism and Inheritance (Method Overriding)

# We can redefine certain methods and attributes specifically to fit the child class, which is known as 
# Method Overriding.

# Polymorphism allows us to access these overridden methods and attributes that have the same name as the
# parent class. Let's look at an example:

# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass
    
#     def __str__(self):
#         return self.name
    
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2

# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.area())
