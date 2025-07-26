# number = int(input("Enter the number: "))
# for i in range(1, number + 1):
#     print(" " * (number - i) + "*" * i)

# def print_count():
#     text = input("Enter a text: ")
#     count = 0
#     for i in text:
#         if i == 'e':
#             count += 1
#     print(count)
# print_count()

# def generate_list(length, start):
#     result = []
#     for i in range (length):
#         start+=i
#         result.append(start)
#     return result
# print(generate_list(10,20))

# def View_info (name , email):
#     emails = ['menoufia@menoufia.com','menoufia2@menoufia.com']
#     if name == '':
#         print("Name is not required")
#     elif email in emails:
#         print("the email is used and error to view your info")
#     else:
#         emails.append(email)
#         print(emails)
#         print(f"Name is : {name} and your email is {email}")
# View_info("Abdallah" , "menoufia3@menoufia.com")

# def read_input():
#     count, total = 0, 0
#     while True:
#         user_input = input("Enter your input : ")
#         if user_input == "done":
#             break
#         else:
#             number = int(user_input)
#             total += number
#             count += 1
#     if count > 0 :
#         print(total)
# read_input()


# def sort_numbers ():
#     numbers = []
#     for i in range (5):
#        while True :
#           num = int(input(f"Enter numbers{i+1}:"))
#           numbers.append(num)
#           break
#     print(sorted(numbers))
#     print(sorted(numbers , reverse=True))
# sort_numbers()

# def find_letter ():
#     letter = input("Enter letter:")
#     text = input("Enter text:")
#     if letter.lower() in text.lower():
#         print(f"The letter {letter} is in the text {text}")
#     else:
#         print("The letter not found")
# find_letter()

# def find_max_low ():
#     numbers = set(map(int, input("Enter your numbers:").split()))
#     max_num = max(numbers[1:-1])
#     min_num = min(numbers[1:-1])
#     print(f"Max number is : {max_num} and min number is : {min_num}")
# find_max_low()

# def prime():
#     number = int(input("enter your number:"))
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return "not prime"
#     return "prime"
# print(prime())

