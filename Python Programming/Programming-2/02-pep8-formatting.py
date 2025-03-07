
# PEP 8: Style Guide for Python Code
# PEP 8 is the official style guide for Python, providing conventions for writing clean, readable, 
# and consistent Python code. 


# PEP 8 Guidelines:
    
# 1. Code Layout

# Indentation
# Use 4 spaces per indentation level. Avoid tabs.

# Example:

def my_function():
    if True:
        print("Hello, World!")
        
        
# Maximum Line Length
# Limit all lines to a maximum of 79 characters.
# For long strings or comments, limit to 72 characters.

# Line Breaks
# Use backslashes (\) or parentheses to break long lines.

# Example:

total = (first_variable
         + second_variable
         + third_variable)


# 2. Blank Lines
# Separate top-level function and class definitions with two blank lines.
# Use one blank line to separate methods inside a class.
# Use blank lines  inside functions to indicate logical sections.


# 3. Imports
# Place imports at the top of the file.

# Follow this order:

# Standard library imports.
# Related third-party imports.
# Local application-specific imports.

# Example:

import os
import sys

import requests

from mymodule import myfunction



# Use one import per line.

import os
import sys  # Preferred

import os, sys  # Not recommended


# 4. String Quotes
# Use single quotes (') or double quotes (") consistently throughout the project.

# Example:

my_string = "Hello"
another_string = 'World'


# 5. Whitespace
# Avoid unnecessary whitespace in the following scenarios:
# Inside parentheses, brackets, or braces

my_list = [1, 2, 3]  # Correct
my_list = [ 1, 2, 3 ]  # Incorrect

print(a, b)  # Correct
print(a , b)  # Incorrect

x = 5 + 3  # Correct
x = 5+3  # Incorrect


# 6. Naming Conventions
# Modules and Variables
# Use lowercase_with_underscores for module names and variables.

my_variable = 10

# Classes
# Use CapWords (PascalCase) for class names.

class MyClass:
    pass

# Constants
# Use UPPERCASE_WITH_UNDERSCORES for constants.

MAX_VALUE = 100

# Functions and Methods
# Use lowercase_with_underscores for function and method names.

def my_function():
    pass


# 7. Comments

# Inline Comments
# Write inline comments and place them after at least two spaces from the code.

x = x + 1  # Increment x by 1

# Block Comments
# Use complete sentences and capitalize the first word.

# This is a block comment.
# It spans multiple lines.


# Docstrings
# Use triple quotes for docstrings ("""), and keep them concise but informative.

def my_function():
    """This function does something amazing."""
    pass


# 8. Classes and Functions
# Class Definitions
# Use two blank lines before the class definition.

class MyClass:
    pass

# Methods in a Class
# Use a single blank line between methods in a class.

class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass
    

# Default Arguments
# Avoid using mutable objects like lists or dictionaries as default arguments.

def my_function(arg=None):
    if arg is None:
        arg = []
        
# 9. Operators
# Place a single space around operators.

a = b + c  # Correct
a=b+c  # Incorrect

# Avoid spaces around = in keyword arguments.
def my_function(a=1):
    pass


# 10. Exceptions
# Use specific exception types.
# Use raise to propagate exceptions.

try:
    x = int("abc")
except ValueError:
    print("Invalid input")
    