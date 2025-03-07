# region 1- Dictionary
"""
This experiment mainly introduces related knowledge units about dictionaries in Python, 
and related operations on them.
- Python dictionary. 
A dictionary has a data structure similar to a mobile phone list, 
which lists names and their associated information. 
In a dictionary, the name is called a "key", 
and its associated information is called "value". 
A dictionary is a combination of keys and values.
- Its basic format is as follows:
d = {key1 : value1, key2 : value2 }
- You can separate a key and a value with a colon, 
separate each key/value pair with a comma, 
and include the dictionary in a brace.
- Some notes about keys in a dictionary: Keys must be unique, 
and must be simple objects like strings, integers, floating numbers, and bool values.
"""
# endregion

# region 2- Create a dictionary
"""
- You can create a dictionary by placing a comma-separated sequence of key-value pairs within braces.
- The following is an example of creating a dictionary:
"""
# Create a dictionary
a = {'one': 1,'two': 2, 'three': 3}
print(a)

b = dict(one=1, two=2, three=3)
print(b)

c = dict([('one', 1), ('two', 2), ('three', 3)]) # list of tuples 
print(c)

d = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # order kyes = values
print(d)

e = dict({'one': 1, 'two': 2, 'three': 3})
print(e)

print(a==b==c==d==e)


data = [("John","CEO",7),("Nacy","hr",7),("LiLei","engineer",9)]

for name, work,age in data:
    employee = {name:(work,age)}

employee1 = {name:(work,age) for name, work,age in data}

print(employee)
print(employee1)
#endregion

# region 3- Accessing dictionary values
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}
my_cat['age_years'] = 2
print(my_cat)

print(my_cat['size']) # fat
# print(my_cat['eye_color'])  # KeyError: 'eye_color'

print(my_cat.get('size')) # fat
print(my_cat.get('eye_color')) # None
#endregion

# region 4- values(), keys(), items()
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}
print(my_cat.keys()) # dict_keys(['size', 'color', 'disposition'])
print(my_cat.values()) # dict_values(['fat', 'gray', 'loud'])
print(my_cat.items()) # dict_items([('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')])
#endregion

# region 5- Checking whether a key or value exists in a dictionary
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}
print('size' in my_cat) # True
print('eye_color' in my_cat) # False
print('fat' in my_cat.values()) # True
print('skinny' in my_cat.values()) # False
#endregion

# region 6-Changing values in a dictionary
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}

my_cat['size'] = 'skinny'
print(my_cat) # {'size': 'skinny', 'color': 'gray', 'disposition': 'loud'}
#endregion

# region 7- Adding new key-value pairs
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}
my_cat['age_years'] = 2
print(my_cat) # {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age_years': 2}
#endregion

# region 8- Removing key-value pairs
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
'age_years': 2,
}
## pop() method
print(my_cat.pop('size')) # fat
print(my_cat) # {'color': 'gray', 'disposition': 'loud', 'age_years': 2}

## popitem() method
print(my_cat.popitem()) # ('age_years', 2)
print(my_cat) # {'color': 'gray', 'disposition': 'loud'}

## del statement
del my_cat['color']
print(my_cat) # {'disposition': 'loud'}

## clear() method
my_cat.clear()
print(my_cat) # {}
#endregion

# region 9- Copying a dictionary
my_cat = {
'size': 'fat',
'color': 'gray',
'disposition': 'loud',
}
my_cat_copy = my_cat.copy()
my_cat_copy['size'] = 'skinny'
print(my_cat_copy) # {'size': 'skinny', 'color': 'gray', 'disposition': 'loud'}
print(my_cat) # {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#endregion




