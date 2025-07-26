# OOP
# class Employee:
#     company_name = "ITI"

#     def __init__(self, name):
#         self.name = name
#         self.age = 20

#     def work(self):
#         print(f"{self.name} is working")

#     def break_for_employee(self):
#         print(f"{self.name} is taking a break")

#     @classmethod
#     def change_company_name(cls, new_name):
#         if len(new_name) > 2:
#             cls.company_name = new_name
#             print("name changed")
#         else:
#             print("Invalid name")

#     @staticmethod
#     def is_valid_salary(value):
#         if value < 1000:
#             print("Invalid salary")
#         else:
#             print("good salary")


# emp = Employee("Mohamed")
# emp2 = Employee("Ahmed")
# emp.work()
# emp2.work()
# emp.break_for_employee()
# print(emp.name)
# print(emp2.name)
# Employee.company_name = "N"
# print(emp.company_name)
# print(emp2.company_name)

# Employee.change_company_name("NTI")
# print(Employee.company_name)

# Employee.is_valid_salary(1200)


# ======================
# special - dunder - magic methods


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# def __str__(self):
#     return f"{self.name}"

# def __eq__(self, other):
#     return self.salary == other.salary

# def __lt__(self, other):
#     return self.salary < other.salary

# def __add__(self, other):
#     return self.name + " " + other.name


# emp = Employee("Mohamed", 1000)
# emp2 = Employee("Ahmed", 2000)
# print(emp != emp2)
# print(e mp + emp2)salary
# sum = emp + emp2
# print(sum)


#  ==================
# encapsulation

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary

# @salary.setter
# def salary(self, value):
#     if value < 1000:
#         print("Invalid salary")
#     else:
#         self.__salary = value

# @salary.deleter
# def salary(self):
#     del self.__salary
# def get_salary(self):
#     return self.__salary

# def set_salary(slef, value):
#     if value < 1000:
#         print("Invalid salary")
#     else:
#         slef.__salary = value


# emp = Employee("Mohamed", 1000)
# print(emp.__dict__)
# print(emp.salary)
# emp.set_salary(-15000)
# print(emp.get_salary())
# emp.salary = 1500
# del emp.salary
# print(emp.salary)


# =================================
# Inheritance
# DRY => Don't Repeat Yourself

# parent , base
# class Human:
#     def __init__(self):
#         self.name = "Mohamed"
#         print("Human constructor")

#     def eat(self):
#         print("Human is eating")

# # child , sub


# class Employee(Human):
#     def __init__(self):
#         super().eat()
#         print("Employee constructor")
#         self.em_num = 2

#     def work(self):
#         print("Employee is working")


# class Student(Human):
#     def study(self):
#         print("Student is studying")


# st = Student()
# emp = Employee()
# st.eat()
# emp.eat()
# print(st.name)
# print(emp.em_num)
# print(emp.name)
# =======================
# multi-level inheritance

# class Human:
#     def __init__(self):
#         self.name = "Mohamed"

#     def eat(self):
#         print("Human is eating")


# class Employee(Human):
#     def work(self):
#         print("Employee is working")


# class Manager(Employee):
#     pass


# m = Manager()
# m.eat()

# ==================================
# multiple inheritance

# class Human:
#     def __init__(self):
#         self.name = "Mohamed"

#     def eat(self):
#         print("Human is eating")


# class Employee():
#     def work(self):
#         print("Employee is working")

#     def eat(self):
#         print("Employee is eating")


# class Freelancer (Human, Employee):
#     pass


# fre = Freelancer()
# fre.eat()


# =======================
# Abstract
# from abc import ABC, abstractmethod


# class Camera(ABC):
#     def take_photo(self):
#         print("Camera is taking a photo")

#     @abstractmethod
#     def record_video(self):
#         pass


# class Sony(Camera):
#     def record_video(self):
#         print("Sony is recording a video with 1080p")


# class Canon(Camera):
#     def record_video(self):
#         print("Canon is recording a video with 720p")


# camera = Camera()
# sony = Sony()
# canon = Canon()

# # sony.record_video()
# # canon.record_video()
# camera.record_video()

# ============================
# Polymorphism

# class Sony():
#     def record_video(self):
#         print("Sony is recording a video with 1080p")


# class Canon():
#     def record_video(self):
#         print("Canon is recording a video with 720p")


# def record_video(cameras):
#     for camera in cameras:
#         camera.record_video()


# sony = Sony()
# canon = Canon()

# record_video([sony, canon])

# print(isinstance(sony, Sony))
# print(sony.issubclass(Sony))
# =========================
# Duck typing
#  if it walks like a duck , and quacks like a duck it is a duck

# class Sony():
#     def record_video(self):
#         print("Sony is recording a video with 1080p")


class Canon():
    def record_video(self):
        print("Canon is recording a video with 720p")


# class Employee:
#     def record_video(self):
#         print("Employee is recording a video with 720p")


# def record_video(cameras):
#     for camera in cameras:
#         camera.record_video()


# sony = Sony()
# canon = Canon()
# emp = Employee()

# record_video([sony, canon, emp])


# ==========================
# Abstraction

class Canon():
    def record_video(self):
        print("Canon is recording a video with 720p")

    def __check_memory(self):
        print("Canon is checking memory")
