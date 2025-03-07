# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 20:46:32 2023

@author: ascom
"""

"""
A Class in Python has three types of access modifiers:
    
    Public Access Modifier
    Protected Access Modifier
    Private Access Modifier
"""



"""
Public Access Modifier: 
    
    All data members and member functions of a class are public by default. 
"""

class Person(object):

 	# __init__ is known as the constructor
 	def __init__(self, name, idnumber):
         self.name = name
         self.idnumber = idnumber

 	def display(self):
         print(self.name)
         print(self.idnumber)



obj = Person("Khalid", 257853)

# accessing public data member
print("Name: ", obj.name)
print("Id: ", obj.idnumber)


# calling public member function of the class
obj.display()


"""
Protected Access Modifier:
    The members of a class that are declared protected are only accessible to a class derived 
    from it. Data members of a class are declared protected by adding a single underscore ‘_’ 
"""

# program to illustrate protected access modifier in a class

# super class
class Student:
	
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch): 
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function 
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)


# # derived class
class Geek(Student):

	# constructor 
	def __init__(self, name, roll, branch): 
         Student.__init__(self, name, roll, branch) 
		
	# public member function 
	def displayDetails(self):
         # accessing protected data members of super class 
         print("Name: ", self._name) 
		 # accessing protected member functions of super class 
         self._displayRollAndBranch()

# creating objects of the derived class	 
obj = Geek("Ali", 1706256, "Information Technology") 

# calling public member functions of the class
obj.displayDetails() 





"""
Private Access Modifier:
    The members of a class that are declared private are accessible within the class only, 
    Data members of a class are declared private by adding a double underscore ‘__’
"""

# program to illustrate private access modifier in a class

class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function 
	def __displayDetails(self):
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
		# accessing private member function
		self.__displayDetails() 

	# getter method for name
	def get_name(self):
		self.__name 
        
	# setter method name
	def set_name(self , name):
		self.__name = name 

	# getter method for roll
	def get_roll(self):
		self.__roll
        
	# setter method roll
	def set_roll(self , roll):
		self.__roll = roll 

	# getter method for branch
	def get_branch(self):
		self.__branch
        
	# setter method branch
	def set_branch(self , branch):
		self.__branch = branch 

             
# creating object 
obj = Geek("Osama", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
