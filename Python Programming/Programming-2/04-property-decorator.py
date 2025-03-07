# The @property Decorator in Python
# is used to define methods in a class that can be accessed like attributes. It allows you to create read-only, computed, 
# or dynamically managed attributes while still maintaining a clean syntax.

# Why Use the @property Decorator?
# Encapsulation: It helps control access to an attribute while preserving the object-oriented principle of encapsulation.
# Computed Attributes: You can define attributes whose values are calculated dynamically.
# Read-Only Attributes: Prevent modification of certain attributes while exposing them for read access.
# Clean Syntax: Instead of calling a method, you can use the familiar obj.attr syntax.
# How It Works

# Basic Example of @property

class Circle:
    def __init__(self, radius):
        self._radius = radius  # protected attribute

    @property
    def radius(self):
        """Getter for the radius attribute."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for the radius attribute."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        """Read-only computed attribute."""
        return 3.14159 * (self._radius ** 2)

# Example Usage
circle = Circle(5)
print(circle.radius)  # Access radius using the getter -> Output: 5
print(circle.area)    # Access computed area -> Output: 78.53975

circle.radius = 10    # Update radius using the setter
print(circle.area)    # Updated area -> Output: 314.159

# circle.radius = -1  # Raises ValueError: Radius cannot be negative


# Defining Getters, Setters, and Deleters
# Getter Method
#     Use @property to define a getter.
# Setter Method
#     Use @property_name.setter to define a setter for the property.
# Deleter Method
#     Use @property_name.deleter to define a deleter for the property.
# Full Example

class Employee:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        """Getter for full_name."""
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, value):
        """Setter for full_name."""
        first, last = value.split()
        self._first_name = first
        self._last_name = last

    @full_name.deleter
    def full_name(self):
        """Deleter for full_name."""
        print("Deleting full_name")
        self._first_name = None
        self._last_name = None

# Example Usage
employee = Employee("John", "Doe")
print(employee.full_name)  # Output: John Doe

employee.full_name = "Jane Smith"  # Use the setter
print(employee.full_name)  # Output: Jane Smith

del employee.full_name  # Use the deleter
print(employee.full_name)  # Output: None None