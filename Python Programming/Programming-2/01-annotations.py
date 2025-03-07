
# Annotations in Python

# are a way to attach additional metadata to variables, function parameters, and return values. They don't 
# affect the runtime behavior of the code but are often used to provide type hints, aiding readability, debugging.


# Where Are Annotations Used?
#     Function Annotations: Describe the expected types of arguments and return values.
#     Variable Annotations: Specify the type of variables.
    
    
# Function annotations are added by appending a colon (:) after the parameter name, followed by the type, 
# and using -> to indicate the return type.


def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

# How to Access Function Annotations
# Annotations are stored in the __annotations__ attribute of the function.

print(greet.__annotations__)
# Output: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}


# Variable annotations specify the type of a variable. Introduced in Python 3.6, they are purely 
# for documentation and static analysis.

class Person:
    name: str
    age: int

print(Person.__annotations__)
# Output: {'name': <class 'str'>, 'age': <class 'int'>}


# Annotations with Complex Types
# Python provides the typing module for complex type annotations.

# Examples
# Lists, Tuples, and Dictionaries
from typing import List, Tuple, Dict

def process_data(items: List[int], mapping: Dict[str, int]) -> Tuple[int, int]:
    return sum(items), len(mapping)


# Optional Types Use Optional to indicate a value could be None.
from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# Union Use Union to specify multiple possible types.
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> float:
    return x + y


# Callable Use Callable to indicate a parameter is a function.
from typing import Callable

def execute(func: Callable[[int , int], int], a: int, b: int) -> int:
    return func(a, b)
