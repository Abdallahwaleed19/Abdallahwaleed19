# Docstrings in Python

# A docstring (short for documentation string) is a string literal used to document a Python module, class, 
# function, or method. Docstrings provide a convenient way to describe the purpose, behavior, and usage of code, 
# making it easier for others.


# Types of Docstrings

# 1. Module-Level Docstring
# Describes the purpose and contents of a module.

"""
This module provides basic mathematical operations.
"""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


# 2. Class-Level Docstring
# Explains the purpose of a class and optionally describes its attributes and methods.

class Calculator:
    """
    A simple calculator class for basic arithmetic operations.

    Methods:
        add(a, b): Returns the sum of two numbers.
        subtract(a, b): Returns the difference between two numbers.
    """
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        return a - b
    
    
# 3. Function or Method-Level Docstring
# Describes what the function or method does, its parameters, and its return value.

def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b


# Formatting Docstrings

# 1. PEP 257
# Python's official guidelines for writing docstrings:

# Use triple quotes for all docstrings.
# The first line should be a short summary of the object’s purpose.
# Add a blank line after the summary if additional explanation is included.
# Keep line length within 72 characters for compatibility.


# 2. Google Style
# A widely adopted format for detailed docstrings.

def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b
    
    
# 3. NumPy Style
# Popular in scientific computing and data analysis.

def square_root(x):
    """
    Compute the square root of a number.

    Parameters
    ----------
    x : float
        The number to find the square root of.

    Returns
    -------
    float
        The square root of the number.
    """
    return x ** 0.5
    
    
# Accessing Docstrings
# Docstrings are stored in the __doc__ attribute of the object.

def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

print(greet.__doc__)  # Output: Greet a person by their name.








