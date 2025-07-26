# number = 10
# our_list = ["anything", 10, 25.2, True]
# print(our_list[1:])

# our_tuple = ("anything", 10, 25.2, True)
# print(our_tuple[1:])

# =====================
# loop

# print("this is anything")

# sentence = "hi this is me"

# for letter in sentence:
#     print(letter, end=" ")

fruits = ["Apple", "Banana", "Kiwi", "Orange", "Mango"]

# for fruit in fruits:
#     # print(fruit)
#     print("hi this is me")


# for fruit in fruits:
#     if fruit == "Kiwi":
#         continue
#     print(fruit)

# for fruit in fruits:
#     if fruit == "Kiwi":
#         break
#     print(fruit)

# for fruit in fruits:
#     pass

# range(stop)
# range(start, stop)
# range(start, stop, step)
# numbers = range(1, 10, 2)
# print(numbers)
# print(type(numbers))

# for number in range(15, 0, -2):
#     print(number)
#     if number == 6:
#         break
# else:
#     print("done")

# for number in range(51):
#     if number in [10, 20, 30, 40, 50, 42]:
#         continue
#     if number == 42:
#         break
#     print(number)
# else:
#     print("done")

# ========================
# while
# i = 0
# while i < 5:
#     pass


# =================
#  functions

# def my_function(x):
#     print("this from out function", x)


# my_function(10)

# def sum_to_numbers(number1, number2, *args):
#     print(number2, number1)
#     print(args[0:2])


# sum_to_numbers(10, 20, 20, 30, 40)
# sum_to_numbers(1, 2)
# sum_to_numbers(5, 20)


# def sum_to_numbers(number2, number1):
#     print(number1)
#     print(number2)


# sum_to_numbers(number1=10, number2=20)

# def create_email(fname, age):
#     print(f"{fname}{10+20}@gmail.com")


# print(create_email("mohamed", 25))


# Return Functions

# def sum_to_numbers(number2, number1):
#     return number1+number2


# sum = sum_to_numbers(10, 20)
# print(sum + 10)

# Default parameters

# def name_of_the_country(country="Egypt"):
#     print("i am from " + country)


# name_of_the_country("UK")

# ==========================

# list , tuple , set , dictionary

# our_list = ["anything", 10, True]
# another = list(("anythign", 10, True))

# print(another)
# print(our_list[1:3])
# print(len(our_list))

# if True in our_list:
#     print("exist")

# our_list[0:2] = ["edit"]

# our_list.append("after append")
# our_list.insert(1, "from insert")
# our_list.extend([10, 20])

# remove from list

# our_list.pop()
# our_list.pop()
# our_list.pop(1)
# our_list.remove(10)
# our_list.clear()
# del our_list
# print(our_list)

# if 60 in our_list:
#     print(our_list.index(60))
# our_list = ["apple", "orange", "orange","kiwi", "banana"]
# our_list_numbers = [10, 50, 2, 30]
# # our_list.sort()
# our_list_numbers.sort(reverse=True)
# our_list.reverse()
# second_list = our_list.copy()
# second_list = list(our_list)
# second_list = our_list[:]
# print(second_list)

# for item in our_list:
#     print(item)

# ============================
#  Tuples - ordered , allow duplicate , unchangable

# our_tuple = ("apple", "orange", "orange", "kiwi", "banana")
# other = tuple(("apple", "orange", "orange", "kiwi", "banana"))
# print(other)
# print(our_tuple[-3:-1])

# if "orange" in our_tuple:
#     print("exist")
# our_tuple[1] = "lkdjfs"

# our_tuple = list(our_tuple)
# our_tuple.pop()
# our_tuple.append("jlkdsjf")
# print(our_tuple)
# our_tuple = tuple(our_tuple)
# print(our_tuple)


# our_tuple = our_tuple + other
# our_tuple += other
# del our_tuple
# our_tuple = ("apple", "orange", "orange", "kiwi", "banana", "orange", "orange")

# a, *b = our_tuple
# coutn_item = our_tuple.count("orange")
# coutn_item = our_tuple.index("orange")
# our_tuple = ("apple",)
# print(type(our_tuple))
# ============================

# Set unordered , unchangable , not allow duplicate

# our_set = {"apple", "orange", "orange", "kiwi", "banana"}
# other = set(("apple", "orange", "orange", "kiwi", "banana"))
# print(our_set[0])
# if "apple" in our_set:
# print("exist")
# if "kljsdf" in our_set:
#     our_set.remove("kljsdf")

# our_set.discard("sdfasdf")
# our_set.pop()
# print(our_set)
#
# our_set = {"apple", "orange", "orange", "kiwi", "banana"}
# other = set((10, 20, "orange", "kiwi", "banana"))

# set3 = our_set.union(other)
# set3 = our_set | other

# set3 = our_set.difference(other)
# set3 = our_set - other
# our_set.difference_update(other)

# set3 = our_set.symmetric_difference(other)
# our_set.symmetric_difference_update(other)
# print(our_set)

#  =========================

# Dictionary ordered from 3.7 , chanagble , not allow duplicat in keyies
# our_dict = {"name": "Mohamed", "country": "Egypt", "age": 25}
# print(our_dict["country"])
# print(our_dict.get("country"))
# print(our_dict.items())
# print(our_dict.keys())
# print(our_dict.values())

# for key in our_dict.keys():
#     print(key, our_dict[key])

# for key, value in our_dict.items():
#     print(key, value)
# our_dict["age"] = 30
# our_dict["wight"] = 60

# print(our_dict)

# if "age" in our_dict:
#     print("exist")

# our_dict.update({"age": 35})
# our_dict.popitem()
# our_dict.popitem()
# our_dict.pop("age")
# del our_dict
# our_dict.clear()
# second_dict = our_dict.copy()
our_dict = {"employee1": {"name": "MOhamed", "age": 25},
            "employee2": {"name": "Ahmed", "age": 30}, }
print(our_dict["employee1"]["name"])
