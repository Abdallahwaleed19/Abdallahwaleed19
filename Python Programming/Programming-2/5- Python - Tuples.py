# region 1- Tuples
# Tuples are similar to lists but they are immutable which means they cannot be changed.
# You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.
# Tuples are created by placing comma-separated values inside parentheses.

# Example
t = (1, 2, 3)
print(t)

# You can also mix object types
t = ('one', 2)
print(t)

# Use indexing just like we did in lists
print(t[0])

# Slicing just like a list
print(t[-1])

# Basic tuple methods
print(t.index('one'))
print(t.count('one'))

# Immutability
# t[0] = 'change'  # This will give an error
# endregion

# region 2- When to use Tuples
# You may be wondering, "Why bother using tuples when they have fewer available methods?"
# To be honest, tuples are not used as often as lists in programming, but are used when immutability is necessary.
# If in your program you are passing around an object and need to make sure it does not get changed, then a tuple becomes your solution.
# It provides a convenient source of data integrity.
# endregion

# region 3- Conversion between data types (List and Tuple)
# You can convert between tuples and lists.
# Just use the tuple() and list() functions.
# Example
my_list = [1, 2, 3]
print(my_list)
print(tuple(my_list))

my_tuple = (1, 2, 3)
print(my_tuple)
print(list(my_tuple))
# endregion

# region 4- Forms of Tuple
t2=(1,)
t3=(1)
t4=3,4
t5=3,t4
print(t5)   
print(type(t2)) # Output: <class 'tuple'>    
print(type(t3)) # Output: <class 'int'>
print(type(t4)) # Output: <class 'tuple'>
print(type(t5)) # Output: <class 'tuple'>

cn=('yi','er','san')
en=('one','two','three')
num=(1,2,3)
x='ali'
tmp=['x',x,cn,en,num,[1.1,2.2],'language']
print(tmp[2])
print(tmp[2][1])
print(tmp[2][1][1])

a= ('ali','mohamed','x',"5")
for i in a:  # i='ali' > j='a' > j='l' > j='i'   
    for j in i:
        print(j,end="\t")
    print()
# endregion

# region - Conclusion
# You should now be able to create and use tuples in your programming as well as have an understanding of their immutability.
# endregion



