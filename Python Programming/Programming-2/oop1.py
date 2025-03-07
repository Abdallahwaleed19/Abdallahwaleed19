# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:15:31 2023

@author: ascom
"""
class FirstClass: # Define a class object
     def setdata(self, value): # Define class methods
         self.data = value # self is the instance
     def display(self):
         print(self.data) 
         
         
         
x = FirstClass() # Make two instances
y = FirstClass() # Each is a new namespace


print(x)
print(y)
print(isinstance(x, FirstClass))

print("##########################")

x.setdata("Ahmed") # Runs: FirstClass.setdata(y, Ahmed)
y.setdata(3.14159) # Runs: FirstClass.setdata(y, 3.14159)
x.display()
y.display()

print("##########################")

x.data = "New value" # Can get/set attributes
x.display()

print("##########################")

x.anothername = "spam" # Can set new attributes here too!
print(x.anothername)

