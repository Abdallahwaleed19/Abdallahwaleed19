# region 1- List Declaration
## List Declaration
## List is a collection which is ordered and changeable. Allows duplicate members.
## In Python lists are written with square brackets.
## List items are ordered, changeable, and allow duplicate values.
## List items are indexed, the first item has index [0], the second item has index [1] etc.
## When we say that lists are ordered, it means that the items have a defined order, 
## and that order will not change.
## Example
## Create a List:

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# endregion

# region 2- Getting values with indexes
## You access the list items by referring to the index number:
## Example
## Print the second item of the list:

# furniture = ['table', 'chair', 'rack', 'shelf']
# print(furniture[0])  # This will give the first element of the list
# print(furniture[1])  # This will give the second element of the list
# print(furniture[2])  # This will give the third element of the list
# print(furniture[3])  # This will give the fourth element of the list
# # print(furniture[4])  # This will give an error
# print(furniture[-1]) # This will give the last element of the list
# print(furniture[-2]) # This will give the second last element of the list
# print(furniture[-3]) # This will give the third last element of the list
# print(furniture[-4]) # This will give the fourth last element of the list
## print(furniture[-5]) # This will give an error

# endregion

# region 3- Getting sublists with slicing
## Slicing a list
## You can specify a range of indexes by specifying where to start and where to end the range.
## When specifying a range, the return value will be a new list with the specified items.
## Example
## Return the third, fourth, and fifth item:

# furniture = ['table', 'chair', 'rack', 'shelf', 'sofa', 'bed']
# print(furniture[2:5])     # This will give the third, fourth, and fifth element of the list
# print(furniture[:4])      # This will give the first, second, third, and fourth element of the list
# print(furniture[2:])      # This will give the third, fourth, fifth, and sixth element of the list
# print(furniture[:])       # This will give the whole list
# print(furniture[1:5:2])   # This will give the second and fourth element of the list
# print(furniture[0:-1])    # This will give the first, second, third, fourth, and fifth element of the list
# print(furniture[0:-1:2])  # This will give the first, third, and fifth element of the list

# endregion

# region 4- Changing values with indexes
## Change the second item:

furniture = ['table', 'chair', 'rack', 'shelf']
furniture[1] = "couch"
print(furniture)

# endregion

# region 5 - Concatenating and Replicating lists
## Concatenating lists
## You can join two or more lists using the + operator:
## Example
## Join two list:

# furniture = ['table', 'chair', 'rack', 'shelf']
# colors = ['red', 'blue', 'green', 'yellow']
# total = furniture + colors
# print(total)

## extend() method
## There are several ways to join, or concatenate, two or more lists in Python.
## One of the easiest ways are by using the + operator.
## Another way to join two lists are by appending all the items from list2 into list1, one by one:
## Example
## Append list2 into list1:

# furniture = ['table', 'chair', 'rack', 'shelf']
# colors = ['red', 'blue', 'green', 'yellow']
# furniture.extend(colors)
# print(furniture) # ['table', 'chair', 'rack', 'shelf', 'red', 'blue', 'green', 'yellow']
# print(colors) # ['red', 'blue', 'green', 'yellow']

## Replicating lists
## If you want to multiply the content of a list n times, you can use the * operator:
## Example
## Multiply the colors list by 2:

# print(colors * 2)   # ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow']

# endregion

# region 6- Looping through a list
## Loop Through a List
## You can loop through the list items by using a for loop:
## Example
## Print all items in the list, one by one:

# furniture = ['table', 'chair', 'rack', 'shelf']
# for x in furniture:
#     print(x)
    
## Loop in Multiple Lists with zip()
## If you want to loop through two lists at the same time, you can use the zip() function.
## Example
## Loop through two lists at the same time:

# furniture = ['table', 'chair', 'rack', 'shelf']
# colors = ['red', 'blue', 'green', 'yellow']
# for item, color in zip(furniture, colors):
#     print(f'furniture: {item} - color: {color}')
    
# endregion

# region 7- The in and not in operators
## Check if Item Exists
## To determine if a specified item is present in a list use the in keyword:
## Example
## Check if "apple" is present in the list:

# furniture = ['table', 'chair', 'rack', 'shelf']
# if "table" in furniture:
#     print("Yes, 'table' is in the furniture list")
# ## Check if "apple" is NOT present in the list:
# if "apple" not in furniture:
#     print("No, 'apple' is not in the furniture list")
    
# endregion

# region 8- The Multiple Assignment Trick
## The multiple assignment trick is a shortcut that allows you to assign multiple variables with the values in a list in one line of code.
## Example
## Assign the elements of a list to multiple variables:

# furniture = ['table', 'chair', 'rack', 'shelf']
# a, b, c, d = furniture
# print(a)
# print(b)
# print(c)
# print(d)

## Instead of
## a = furniture[0]
## b = furniture[1]
## c = furniture[2]
## d = furniture[3]
## The multiple assignment trick can also be used to swap the values in two variables:
## Example
## Swap two variables:

# a, b = 'table', 'chair'
# a, b = b, a
# print(a)
# print(b)

# endregion

# region 9- List Methods
## List Methods
## Python has a set of built-in methods that you can use on lists.
## Method	Description
## append()	Adds an element at the end of the list
## clear()	Removes all the elements from the list
## copy()	Returns a copy of the list
## count()	Returns the number of elements with the specified value
## extend()	Add the elements of a list (or any iterable), to the end of the current list
## index()	Returns the index of the first element with the specified value
## insert()	Adds an element at the specified position
## pop()	Removes the element at the specified position, by default removes the last element
## remove()	Removes the item with the specified value
## reverse()	Reverses the order of the list
## sort()	Sorts the list
## Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
## Example
## Print all methods/attributes of a list object:

# furniture = ['table', 'chair', 'rack', 'shelf']
# print(dir(furniture))

## Adding Values
## To add an item to the end of the list, use the append() method:
## Example
## Add an item to the end of the list:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.append('sofa')
# print(furniture)

## To add an item at the specified index, use the insert() method:
## Example
## Add an item at the specified index:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.insert(1, 'sofa')
# print(furniture)

## Removing Values
## The remove() method removes the specified item:
## Example
## Remove the specified item:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.remove('chair')
# print(furniture)

## The pop() method removes the specified index, (or the last item if index is not specified):
## Example
## Remove the second item:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.pop(1)
# print(furniture)

## The del keyword removes the specified index:
## Example
## Remove the first item:

# furniture = ['table', 'chair', 'rack', 'shelf']
# del furniture[0]
# print(furniture)

## The del keyword can also delete the list completely:
## Example
## Delete the entire list:

# furniture = ['table', 'chair', 'rack', 'shelf']
# del furniture

# print(furniture) # This will cause an error because "furniture" no longer exists.
## The clear() method empties the list:
## Example
## Clear the list content:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.clear()
# print(furniture)

## Sorting the list
## The sort() method sorts the list ascending by default:
## Example
## Sort the list alphabetically:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.sort()
# print(furniture)

## You can also make a function to decide the sorting criteria(s):
## Example
## Sort the list based on the length of the elements:

# def myFunc(e):
    
#     return len(e)
# furniture = ['tables', 'Windows', 'rack', 'shelf']
# furniture.sort(key=myFunc)
# print(furniture) # ['rack', 'shelf', 'tables', 'Windows']

## Sort the list descending:
## Example
## Sort the list descending:

# furniture = ['table', 'chair', 'rack', 'shelf']
# furniture.sort(reverse=True)
# print(furniture)
# numbers = [2, 5, 3.14, 1, -7]
# numbers.sort()
# print(numbers)

# endregion

# region 10- Check if the list is Empty
## Check if the list is empty
## To determine if a list is empty or not, you can use an if statement:
## Example
## Check if the list is empty:

# furniture = []
# if furniture:
#     print("The list is not empty")
# else:
#     print("The list is empty")

# if furniture == []:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# if len(furniture) == 0:
#     print("The list is empty")
# else:
#     print("The list is not empty")

# endregion

# region 11- Copying a list

#Method one by reference:
# old_list=["hello","Jeary",'ali','mohamed','mahmoud','4',5,6]
# print(old_list)
# print(old_list[1:3])
# new_list = old_list  
# print(new_list)
# print(old_list)
# new_list.append('ahmed')
# print(new_list)
# print(old_list)
# print(id(new_list))
# print(id(old_list))

#Method two by value:
##1- Using the slicing method
# new_list2 = old_list[:]  
# new_list2.append('xxxxxxxxxx')
# print(new_list2)
# print(old_list)
# print(id(new_list2))
# print(id(old_list))
# ##2- Using the list() method
# new_list3 = list(old_list)
# new_list3.append('yyyyyyyyyy')
# print(new_list3)
# print(old_list)
# print(id(new_list3))
# print(id(old_list))
##3- Using the copy() method
# new_list4 = old_list.copy()
# new_list4.append('zzzzzzzzzz')
# print(new_list4)
# print(old_list)
# print(id(new_list4))
# print(id(old_list))
##4- Using class module
# from copy import copy
# new_list5 = copy(old_list)
# new_list5.append('wwwwwwwwww')
# print(new_list5)
# print(old_list)
# print(id(new_list5))
# print(id(old_list))
# endregion


