# Scope
# LEGB [Local , Enclosing , Global , Built-in]

# def greeting():
#     name = "Mohamed"
#     print(name)
#     print(name)
#     print(name)


# # print(name)
# greeting()
# x = 100


# def outer():
#     global x
#     x = 300

#     def inner():
#         nonlocal x
#         x = 200
#         print(x)
#     inner()
#     print(x)


# outer()

# name = "Mohamed"


# def our_greetring():
#     global name
#     name = "Ahmed"
#     print(name)


# our_greetring()
# print(name)

# print()
# len()
# =============

# import math_utils

# math_utils.test(10, 20)
# math_utils.sub(10, 20)
# math_utils.mul(10, 20)

# from math_utils import add, sub

# add(10, 20)
# ====================
# import clcualto.math_utils as mu

# mu.add(10, 20)

# from math_utils import *
# add(10, 20)
# sub(10, 20)
# mul(10, 20)
#  ======================
# Packes

# from calculator.basic_operation.math_utils import add

# add(10, 20)

# # print(dir())
# print(__name__)


# ====================
# import math

# print(math.ceil(3.2))

import random
import string
# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([10, 20, 30, 40]))
# print(random.choices([10, 20, 30, 40], k=2))
# our_list = [10, 20, 30, 40]
# random.shuffle(our_list)
# print(our_list)

# print(string.ascii_letters)
# print(string.digits)

# print("".join(random.choices(string.ascii_letters + string.digits + "&%^$##", k=4)))
# from calculator.basic_operation.math_utils import add
# import sys
# print(sys.path)
# =============================
# print("")
# try:
#     number = int(input("enter any number "))
#     print(number / 0)
# except ValueError:
#     print("you must enter a number")
# except NameError:
#     print("this is from name error")
# except Exception as e:
#     # print("this is for any error")
#     print(e)

# print("another code ")


# try:
#     number = int(input("enter any number "))
#     print(number / 0)
# except Exception as e:
#     print(e)
# else:
#     print("there is no erros ")
# finally:
#     print("this will print anyway")

# print("another code ")


# age = 17

# if age < 18:
#     raise Exception("you must be older than 18")


# ================================
#  a -> append , w -> write , r -> read , x -> cereate , rt -> t for text
# f = open("lab3.txt")
# # print(f.read())
# print(f.readlines())

# f.close()

#  with for handling files
#  with open("") as f:

# with open("lab3.txt") as f:
#     print(f.read())

# with open("lab3.txt", "a") as f:
#     print(f.write("this is from append file"))

# with open("lab3.txt" , "w") as f:
#     print(f.read())

# import os

# if os.path.exists("lab30.txt"):
#     os.remove("lab30.txt")

# from pathlib import Path

# p = Path("lab3.txt")
# # p.exists()
# # p.rename("lab2.txt")
# # p.unlink()

# print(p.read_text())


# ================================
