# region 1-Functions
# # Function definition
# def greet():
#     print("Hello!")
# # # Function call
# greet()  # Output: Hello!
# endregion
#
# int add(int a, int b) { return a + b; }


# region 2- Function Parameters
# Function definition
# def greet(name):
#     print(f"Hello, {name}")
# # Function call
# greet("Alice")
# endregion

# region 3- Default Parameters
# Function definition
# def greet(name="Alice"):
#     print(f"Hello, {name}")
# # Function call
# greet()  # Output: Hello, Alice
# greet("Bob")  # Output: Hello, Bob
# endregion

# region 4- Return Statement
# Function definition
# def add(a, b):
#     return a + b
# # Function call
# result = add(10, 20)
# print(result)  # Output: 30
# endregion

# region 5- Multiple Return Values
# # Function definition
# def add_sub(a, b):
#     return a + b, a - b
# # # Function call
# add_result, sub_result = add_sub(10, 20)
# print(add_result)  # Output: 30
# print(sub_result)  # Output: -10
# endregion

# region 6- Scope of Variables
# # Global variable
# num = 10
# # # Function definition
# def func():
#     # Local variable
#     num = 20
#     print(num)
# # Function call
# func()  # Output: 20
# print(num)  # Output: 10
# endregion

# region 7- Global Keyword
# # Global variable
# num = 10
# # Function definition
# def func():
#     # Global keyword
#     global num
#     num = 20
#     print(num)
# # Function call
# func()  # Output: 20
# print(num)  # Output: 20
# endregion

# region 8- Lambda Function
# Lambda function
# add = lambda a, b: a + b
# # Function call
# result = add(10, 20)
# print(result)  # Output: 30
# endregion

# region 9- map() function
# # List of numbers
numbers = [1, 2, 3, 4, 5]
# # # Lambda function
square = lambda x: x ** 2
# # Noraml Function definition Equivalent to the lambda function:
# # def square(x):
# #     return x ** 2
# # map() function
# # Map function is used to apply the function to all the elements of the list, 
# # and return the result as a map object, which can be converted to a list, tuple, or set.
result = map(square, numbers)
print(result)
print(list(result))  # Output: [1, 4, 9, 16, 25]
# endregion

# region 10- filter() function
# # List of numbers
# numbers = [1, 2, 3, 4, 5]
# # # Lambda function
# is_even = lambda x: x % 2 == 0
# # # filter() function
# # # Filter function is used to filter the elements of the list based on the condition provided in the function,
# # # and return the result as a filter object, which can be converted to a list, tuple, or set.
# result = filter(is_even, numbers)
# print(list(result))  # Output: [2, 4]
# endregion

# region 11- Recursive Function
# Function definition

# def factorial(n):
#     if n <= 1:
#         return 1 
#     else:
#         return n * factorial(n - 1)

# # Function call
# result = factorial(1000)
# print(result)  # Output: 120

# endregion
