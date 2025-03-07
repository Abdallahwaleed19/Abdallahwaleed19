# region 1- % Operator

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "John"
age = 23
print("%s is %d years old." % (name, age))  # John is 23 years old.

mylist = [1, 2, 3]
print("A list: %s" % mylist)    # A list: [1, 2, 3]

number = 5.59866
print("Floating point number: %.2f" % number)   # Floating point number: 5.60

print("Hexadecimal number: %X" % 15)    # Hexadecimal number: F
# endregion

# region 2- format() method
# This method lets us concatenate elements within a string through positional formatting.
# The curly braces {} are used as placeholders.
# The format() method returns a formatted string with the value of the variables.

print("Hello, {}!".format(name))  # Hello, John!

print("Hello, {}. You are {}.".format(name, age))  # Hello, John. You are 23.

print("Hello, {0}. You are {1}.".format(name, age))  # Hello, John. You are 23.

print("Hello, {1}. You are {0}.".format(age, name))  # Hello, John. You are 23.

# We can use keyword arguments to format the string.
print("Hello, {name}. You are {age}.".format(name="John", age=23))  # Hello, John. You are 23.

# We can use a mix of positional arguments and keyword arguments.
print("Hello, {0}. You are {age}.".format(name, age=23))  # Hello, John. You are 23.

# We can use the format() method to format integers.
print("The number is: {:d}".format(123))  # The number is: 123 

# We can use the format() method to format floats.
print("The float number is: {:f}".format(123.4567898))  # The float number is: 123.456790

# We can use the format() method to format floats with a specific number of decimal places.
print("The float number is: {:.2f}".format(123.4567898))  # The float number is: 123.46

# endregion

# region 3- f-strings
# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
# f-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
# f-strings are available in Python 3.6 and later versions.

print(f"Hello, {name}!")  # Hello, John!

print(f"Hello, {name}. You are {age}.")  # Hello, John. You are 23.

# We can use the f-string to format integers.
print(f"The number is: {123}")  # The number is: 123

# We can use the f-string to format floats.
print(f"The float number is: {123.4567898}")  # The float number is: 123.456789

# We can use the f-string to format floats with a specific number of decimal places.
print(f"The float number is: {123.4567898:.2f}")  # The float number is: 123.46

"""
Number	    Format	   Output	  description
3.1415926	{:.2f}	   3.14	      Format float 2 decimal places
3.1415926	{:+.2f}	   +3.14	  Format float 2 decimal places with sign
-1	        {:+.2f}	   -1.00	  Format float 2 decimal places with sign
2.71828	    {:.0f}	   3	      Format float with no decimal places
4	        {:0>2d}	   04	      Pad number with zeros (left padding, width 2)
4	        {:x<4d}	   4xxx	      Pad number with x’s (right padding, width 4)
10	        {:x<4d}	   10xx	      Pad number with x’s (right padding, width 4)
1000000	    {:,}	   1,000,000  Number format with comma separator
0.35	    {:.2%}	   35.00%	  Format percentage
1000000000	{:.2e}	   1.00e+09	  Exponent notation
11	        {:11d}	   11	      Right-aligned (default, width 10)
11	        {:<11d}	   11	      Left-aligned (width 10)
11	        {:^11d}	   11	      Center aligned (width 10)
"""
# endregion


