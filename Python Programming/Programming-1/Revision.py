# import _thread
# import time 
# def print_time (Thread_Name , Delay):
#     count = 0
#     while count < 3:
#         time.sleep(Delay)
#         count += 1
#         print (Thread_Name , "..............." , time.ctime())
# try :
#     _thread.start_new_thread(print_time, ("Thread-1" , 2 ,))
#     _thread.start_new_thread(print_time, ("Thread-2" , 2 ,))
# except:
#     print ("Error: unable to start thread")
# while True :
#     pass
      
      
# import threading
# def print_square (num):
#     print("the square = " , num**2)
# def print_cube (num):
#     print("the cube = " , num**3)
# t1 = threading.Thread(target=print_square, args=(10,))
# t2 = threading.Thread(target=print_cube, args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()



# class Validate_order :
#     def validate_order (self , order):
#         print(f"Validating {order}")
# class Update_order :
#     def update_order (self , order):
#         print(f"Updating {order}")
# class Send_notfication :
#     def send_notification (self , order):
#         print(f"Sending notification for {order}")
# class OrderProcessor:
#     def __init__(self, validator, inventory_manager, notifier):
#         self.validator = validator
#         self.inventory_manager = inventory_manager
#         self.notifier = notifier

#     def process_order(self, order):
#         self.validator.validate_order(order)
#         self.inventory_manager.update_order(order)
#         self.notifier.send_notification(order)
# # Usage 

# order_processor = OrderProcessor(Validate_order(), Update_order(), Send_notfication())
# order_processor.process_order("Order-1")


# class Bird :
#     def move (self):
#         pass
# class Flying (Bird):
#     def move (self):
#         print("I am Flying")
# class Moving (Bird):
#     def move (self):
#         print("I am Moving")
# class Penguin (Moving):
#     def move (self):
#         print("I am Penguin and I can Move")
# Bird1 = Penguin()
# Bird1.move()  # Output: I am Penguin and I can Move



# class Machine : 
#     def Doing (self):
#         pass 
# class Printable (Machine):
#     def Doing (self):
#         print("I am Printing")
# class Scanable (Machine):
#     def Doing (self):
#         print("I am Scanning")
# class Faxable (Machine):
#     def Doing (self):
#         print("I am Faxing")
# class Printer (Printable, Scanable):
#     def Doing (self):
#         print("I am Printing and Scanning")
# Machine1 = Printer()
# Machine1.Doing()  # Output: I am Printing and Scanning

# from abc import ABC, abstractmethod
# class Mobile(ABC):
#     @abstractmethod
#     def notification(self):
#         pass
# class SMS_Notification(Mobile):
#     def notification(self):
#         print("SMS Notification")
# class Email_Notification(Mobile):
#     def notification(self):
#         print("Email Notification")
# class Notification_Service:
#     def __init__(self, notification: Mobile):
#         self.notification = notification
#     def Notify(self):
#         self.notification.notification()
#         print("I am Notifying")
# notification1 = SMS_Notification()
# notification2 = Email_Notification()
# notification_service1 = Notification_Service(notification1)
# notification_service1.Notify()
# notification_service2 = Notification_Service(notification2)
# notification_service2.Notify()



# class Reading_File :
#     def __init__(self, file_name):
#         self.file_name = file_name
#     def read_file(self):
#         return "Iam Reading File"
# class Pricessing_Data : 
#     def __init__(self, Data):
#         self.Data = Data
#     def process_data(self):
#         return "Iam Processing Data"
# class Generating_Report : 
#     def __init__(self , Report):
#         self.Report = Report
#     def generate_report(self):
#         return "Iam Generating Report"


# from abc import ABC , abstractclassmethod
# class Shape (ABC) :
#     @abstractclassmethod
#     def area(self):
#         pass
# class Rectangle (Shape):
#     def __init__(self , length , width):
#         self.length = length
#         self.width = width
#     def area (self):
#         return self.length * self.width
# class Circle (Shape):
#     def __init__(self , radius):
#         self.radius = radius
#     def area (self):
#         return 3.14 * self.radius * self.radius
# class Triangle (Shape):
#     def __init__(self , base , height):
#         self.base = base    
#         self.height = height
#     def area (self):
#         return 0.5 * self.base * self.height


# class Bird : 
#     def Eat (self):
#         return "Bird is Eating"
# class Flying_Bird : 
#     def Fly (self):
#         return "Bird is Flying"
# class Moving_Bird :
#     def Move (self):
#         return "Bird is Moving"
# class Penguin (Bird , Moving_Bird):
#     def Eat (self):
#         return "Penguin is Eating"
#     def Move(self):
#         return "Penguin is Moving"
# class Sparrow (Bird , Flying_Bird):
#     def Eat (self):
#         return "Sparrow is Eating"
#     def Fly (self):
#         return "Sparrow is Flying"

# from abc import ABC , abstractclassmethod
# class Printabe (ABC) :
#     @abstractclassmethod
#     def print (self):
#         pass
# class Scanable (ABC) :
#     @abstractclassmethod
#     def scan (self):
#         pass
# class Faxanable (ABC) :
#     @abstractclassmethod
#     def fax (self):
#         pass
# class Printer (Printabe) :
#     def print (self):
#         return "Printing"
# class Scanner (Scanable) :
#     def scan (self):
#         return "Scanning"
    
    
# from abc import ABC , abstractclassmethod
# class Notification (ABC) :
#     @abstractclassmethod
#     def Notify (self) :
#         pass 
# class SMS_Notification (Notification) :
#     def Notify (self) :
#         return "Sending SMS"
# class Notification_services (Notification) :
#     def __init__(self , services : Notification):
#         self.services = services
#     def Notify (self) :
#         return f"Service : {self.services.Notify()}"
# notification = Notification_services (SMS_Notification())
# print (notification.Notify())  


# def Safe_Division (number1:float , number2: float) -> float:
#     if number2 == 0:
#         raise ZeroDivisionError("Error: Division by zero is not allowed")
#     return number1 / number2
# try:
#     print(Safe_Division(10, 10))
# except ZeroDivisionError as e:
#     print(e)

# def Validate_User (Name: str, Age: int) -> str:
#     if Name == "":
#         raise ValueError("Error: Name cannot be empty")
#     if Age < 0:
#         raise ValueError("Error: Age cannot be negative")
#     return f"User  {Name} and his age {Age}"
# try:
#     print(Validate_User ("Abdallah", 20))
# except ValueError as e:
#     print(e)
        
# from typing import List, Dict

# def process_scores(scores: List[float]) -> Dict[str, object]:
#     """
#     Process a list of scores to calculate the average and filter scores above the average.

#     Args:
#         scores (List[float]): A list of numeric scores.

#     Returns:
#         Dict[str, object]: A dictionary with 'average' and 'above_average'.
#     """
#     average = sum(scores) / len(scores)
#     above_average = [score for score in scores if score > average]
#     return {"average": average, "above_average": above_average}


# def Calculate_average (numbers: list[int]) -> int :
#     """ we will calculate the average by : 
#     get the sum of numbers and get the len of numbers and division them = 
#     result = sum(numbers) / len(numbers)"""
#     result = sum(numbers) / len(numbers)
#     return f"result = {result}"
# print(Calculate_average([1, 2, 3, 4, 5]))


# def Reverse_String(name:str) -> str : 
#     """ we will return the reverse of the input string """
#     return name[::-1]
# print(Reverse_String("Abdallah"))

# def Filter_even_numbers (numbers: list[int]) -> list[int]:
#     """ we will return a list of even numbers from the input list """
#     return [num for num in numbers if num % 2 == 0]
# print(Filter_even_numbers([1, 2, 3, 4, 5,6 ,7 ,8 , 9, 10 ]))


# def Filter_and_square (numbers: list[int]) -> list[int]:
#     """ we will return a list ofnumbers from the input list and square them """
#     return [num ** 2 for num in numbers if num > 10]
# print(Filter_and_square([11,12,13,14,15,16]))

# class FileManager:
#     def __init__(self , filename , mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def __enter__ (self):
#         self.file = open(self.filename , self.mode)
#         return self.file
#     def __exit__ (self , exc_type , exc_val , exc_tb):
#         if self.file:
#             self.file.close()
# with FileManager('file.txt', 'r') as file:
#     content = file.read()
#     print(content)

# class My_Sequance :
#     def __init__ (self , data):
#         self.data = data
#     def __getitem__(self , index):
#         return self.data[index]
#     def __len__ (self):
#         return len(self.data)
# my_seq = My_Sequance([1, 2, 3, 4 , 5 , 6 , 7 , 8 , 9 , 10])
# print(my_seq.__getitem__(2))
# print(my_seq.__len__())


# class Book : 
#     def __init__(self , title , author , price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def compare_price(self):
#         return f"This Book {self.title} is more expensive than the other book"
# book1 = Book('Java book' , 'Mark' , 30)
# book2 = Book("Python Programming" , "John Doe" , 25)
# if book1.price > book2.price:
#     print(book1.compare_price())
# else:
#     print(f"This Book {book2.title} is more expensive than the other book")

# class Iterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < self.data:
#             result = self.index
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
# obj1 = Iterator(5)
# for num in obj1:
#     print(num)
    
    
# class Rectangle :
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     @property
#     def area (self):
#         return self.width * self.height
#     @area.setter
#     def area (self , value):
#         if value < 0:
#             raise ValueError("Area cannot be negative")
#         self.width = value / self.height

# rect = Rectangle(5,10)
# print(rect.area)
# rect.area = 60
# print(rect.width)




# import math
# from turtle import *
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#     math.cos(2*k)-2*\
#     math.cos(3*k)-\
#     math.cos(4*k)
# speed(0)
# bgcolor("black")
# for i in range (6000):
#     goto(hearta(i)*20 , heartb(i)*20)
#     for j in range (5):
#         color("red")
#     goto(0,0)
# done()