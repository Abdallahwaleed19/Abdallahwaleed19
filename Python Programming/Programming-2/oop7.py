# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:10:52 2023

@author: ascom
"""

"""
Class or Static Variables

> a static variable is a variable that is shared among all instances of a class, 
    rather than being unique to each instance.
    
> Static variables are defined inside the class definition, but outside of any method definitions. 

> They are typically initialized with a value, just like an instance variable, 
  but they can be accessed and modified through the class itself, rather than through an instance.    
"""





# Python program to show that the variables with a value 
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable (Static)
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"


# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'mech'
print(b.stream) # prints 'mech'
