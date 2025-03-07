# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:50:56 2023

@author: ascom
"""

"""
An abstract class can be considered a blueprint for other classes. 
It allows you to create a set of methods that must be created within 
any child classes built from the abstract class.

A class that contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation.

By default, Python does not provide abstract classes. Python comes with a module that 
provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
"""

# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 


class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 


# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 
