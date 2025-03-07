# -*- coding: utf-8 -*-
"""
    Created on Tue Dec 19 20:24:58 2023
    
    @author: Ahmed
"""

"""
    Exceptions
"""


x = 5 
y = "hello" 
a = [1,2,3]
try: 
    print("Test1")
    print(a[3])
    z = x + y 
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")

    