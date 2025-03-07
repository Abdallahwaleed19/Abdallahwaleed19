# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:02:43 2023

@author: ascom
"""

#Adding properties to child class

# parent class
class Person():
    def __init__(self, name, age):
    	self.name = name
    	self.age = age
    
    def display(self):
    	print(self.name, self.age)
    
    # child class
class Student(Person):
    def __init__(self, name, age, dob):
    	self.dob = dob
    	# inheriting the properties of parent class
    	super().__init__(name, age)
    
    def displayInfo(self):
    	print(self.name, self.age, self.dob)

obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()





# Python example to show the working of multiple
# inheritance

class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()






# A Python program to demonstrate multilevel 

# inheritance 

class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

