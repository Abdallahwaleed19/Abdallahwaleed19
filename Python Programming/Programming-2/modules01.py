# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:07:22 2023

@author: Ahmed
"""

# importing module calc.py
import calc

#print(calc.add(10, 2))

# calc.spam('gumby')



print('-------------------------------')

"""
    Imports Happen Only Once
"""
print(calc.a)  # 1

calc.a = 10   # Change attribute in module
print(calc.a)   #10


import calc   # Just fetches already loaded module

print(calc.a)   # Code wasn't rerun: attribute unchanged

 
print('-------------------------------')

"""
    import Vs. from 
    • import assigns an entire module object to a single name.
    • from assigns one or more names to objects of the same names in another module.
"""


from small import a,b  #copy out a, b into local vars a,b

print(a) #1
print(b)  #[1,2]

a = 20  #changes local a only not the module a
b[0] =15 #changes shared mutbale as list considered a ref obj

print(a)   #20     1
print(b)   #[15,2]

import small   

print(small.a)   #1
print(small.b)   #[15,2]
