# region 1- Defenition
"""
Definition: Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object. 
It helps simplify code by breaking down complex structures into simpler, manageable interfaces.

Importance: Abstraction makes systems easier to understand and reduces complexity. 
In Python, abstract classes and methods can be implemented using the abc (Abstract Base Classes) module.
"""
# Eamples 1: 

from abc import ABCMeta, abstractmethod

# include <iostream>
# include <math.h>
# using namespace std;

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass
        
    @abstractmethod
    def move(self):
        pass

    def eat(self):
        return "Eat"
    

class Dog(Animal):
    # pass
    def sound(self):
        return "Bark"
        
    
    def move(self):
        return "Runs"

class Bird(Animal):
    def sound(self):
        return "Chirp"
    
    def move(self):
        return "Flies"

# Using the classes
# animal = Animal() # This will raise an error
dog = Dog()
print(dog.sound())  # Output: Bark
print(dog.move())   # Output: Runs
print(dog.eat()) 
bird = Bird()
print(bird.sound()) # Output: Chirp
print(bird.move())  # Output: Flies
print(bird.eat())

# Example 2-
# Python program showing
# abstract base class work
from abc import ABCMeta, abstractmethod


class Polygon(metaclass=ABCMeta):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides") 

class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")




# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
#endregion