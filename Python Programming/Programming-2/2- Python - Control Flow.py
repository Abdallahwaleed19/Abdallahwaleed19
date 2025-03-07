# # region 1- If Statement
# num = -5
# if num > 0:
#     print("Positive number")
 
# # endregion

# # region 2- If-Else Statement
# num = -5
# if num > 0:
#     print("Positive number")
# else:
#     print("Negative number")

# # endregion

# # region 3- If-Elif-Else Statement
# num = 0
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

# # endregion

# # region 4- Nested If Statement
# num = 0
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

# # endregion

# # region 5- Short Hand If
# num = 10
# if num > 0: print("Positive number")

# endregion

# # region 6- Short Hand If-Else

# num = 10
# print("Positive number") if num > 0 else print("Negative number")

# # endregion

# # region 7- Short Hand If-Elif-Else
# # num = 0
# print("Positive number") if num > 0 else print("Zero") if num == 0 else print("Negative number")

# # endregion

# region 8- And Operator
# num = 10  
# if num > 0 and num % 2 == 0:
#     print("Positive and Even number")

# endregion

# region 9- Or Operator
# # num = 11
# if num > 0 or num % 2 == 0:
#     print("Positive or Even number")

# endregion

# region 10- Not Operator
# num = 10
# if not num > 0:
#     print("Negative number")

# endregion

# #region 11- Pass Statement
# num = 10
# if num > 0:
#     pass

# endregion

# region 12- Ternary Operator

# num = 10
# result = "Positive number" if num > 0 else "Negative number"
# print(result)


# endregion

# region 13- While Loop

# num = 1
# while num <= 5:
#     print(num)
#     num += 1

# endregion

# region 14- Break Statement
# num = 1
# while num <= 5:
#     if num == 3:
#         break
#     print(num)
#     num += 1

# endregion

# region 15- Continue Statement
# num = 1
# while num <= 5:
#     if num == 3:
#         num += 1
#         continue
#     print(num)
#     num += 1

# endregion

# region 16- For Loop
# my_list = [1, 2, 3, 4, 5]
# for num in my_list:
#     print(num)

# endregion

# region 17- Range Function
for num in range(1, 6):
    print(num)

# endregion

# region 18- Nested Loop
# for i in range(1, 3): # i=1,2
#     for j in range(1, 3): # j=1,2
#         print(i, j)

# endregion

# region 19- Break Statement
# for num in range(1, 6):
#     if num == 3:
#         break
#     print(num)

# endregion

# region 20- Continue Statement
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# endregion



# region 22- Switch Case Statement 
# The Switch-Case statements was officially released with Python 3.10 in September 2022.
# response_code = 400
# match response_code:
#     case 200:
#         print("OK")
#     case 400:
#         print("Bad Request")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Internal Server Error")
#     case _:
#         print("Unknown Response Code")
# endregion
