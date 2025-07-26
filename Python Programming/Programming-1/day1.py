# Data Types:
# numbers  [int , float , complex]
# string
# boolean
# none
# primitive => mutable -  non primitive => immutable

# number = 10.0
# # number1 = -10.2

# # print(type(number))
# # print(type(number1))

# # number = 3j
# # print(type(number))
# # False
# # True

# =======================
# Arithmetic Operators
# # + - * / // % **

# # number = 10 + 20
# # number1 = 10 - 20
# # number3 = 10 * 20
# # number4 = 20 / 10
# # number5 = 5 // 2
# # number6 = 10 % 3
# number7 = 2 ** 2
# # print(number)
# # print(number1)
# # print(number3)
# # print(number4)
# print(number7)


# ==========
# Assignment Operators
#  += -= *= /= //= %= **=

# number = 10
# # number = number + 5
# # number += 5
# number -= 5

# print(number)


# =================
# Comparison Operators
#  > < == >=
# print(10 >= 10)
# print(10 <= 10)
# print(10 != 10)
# ==================
# Logical Operators
# and or not

# true and true = true
# true and false = false
# false and false = false

# or
# true + true = true
# false + true = true
# false + false = false


# print(10 == 10 or 11 != 11)
# ======================
# number methods & functions

# print(abs(-5.2))
# print(round(5.6))


import math

# print(math.ceil(3.1))
# print(math.floor(3.9))
# print(math.sqrt(25))


# number = 10
# number += 5
# print(id(number))

# =================
# String datatype

# sentence = "Hell world!"
# sentence = 'Hell world! and it"s me '
# sentence = """Hell world!
#     this is
#     me
# # """

# senetence = "hello \" world!"
# # sentence = 'hello \' world!'
# # sentence = 'hello \nworld!'
# # sentence = 'hello \tworld!'
# sentence = 'hello \\ world!'
# =================

sentence = "     Hello world laba lab lab      "
# print(sentence[-5:-1])

# print(len(sentence))

# print('mohamed' in sentence)
# sentence = sentence.upper()
# print(sentence.capitalize())
# print(sentence.count("lab"))
# print(sentence.replace("l", 'a'))
# print(sentence.islower())
# print(sentence.split())
# print(sentence.startswith('j'))
# print(sentence.endswith('b'))
# print(sentence.lstrip())
# print(sentence.rstrip())


# ====================
# if Condition

# gender = "male"


# if not age < 18:
#     print("sorry, you can't use our app")
#     # print("this from if")
# elif age < 60:
#     print("Welcome to our app")
# elif age < 60:
#     print("Welcome to our app")
# elif age < 60:
#     print("Welcome to our app")
# elif age < 60:
#     print("Welcome to our app")
# else:
#     print("sorry, you age must be between 19  and 60")
# =======================
# Match

# day = 25

# match day:
#     case 18:
#         print("today is 18")
#     case 19:
#         print("today is 19")
#     case _:
#         print("today is not 18 or 19")


# ========================

# number = int(input("enter an number "))
# number = int(number)
# number += 5
# print(number)

number = 10
# float_number = float(number)

# print(float_number)
# print(type(float_number))

string_number = str(number)
print(string_number)
print(type(string_number))
