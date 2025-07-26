# class Employee :
#     def __init__ (self , name , age , salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def dsiplay_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
# Employee1 = Employee("Abdallah", 20, 50000)
# Employee2 = Employee("Rahma", 20, 60000)
# Employee3 = Employee("Saif", 20, 70000)
# Employee1.dsiplay_info()
# Employee2.dsiplay_info()
# Employee3.dsiplay_info()


# class Employee:
#     company = "ITI"
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Company: {self.company}")
#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company
# Employee1 = Employee("Abdallah", 20, 50000)
# Employee2 = Employee("Rahma", 20, 60000)
# Employee2.change_company("DEPI")
# Employee1.display_info()
# Employee2.display_info()


# class Employee:
#     def __init__ (self , name , age , salary):
#         self.name = name 
#         self.age = age
#         self.salary = salary
#     def calculate_bonus(self):
#         print("No Bonus")
# class Developer (Employee):
#     def __init__(self, name, age, salary , job):
#         super().__init__(name, age, salary)
#         self.job = job
#     def calculate_bonus(self):
#         print(f"Name:{self.name}, job:{self.job} ,  Bonus: {self.salary * 0.1}")
# class Manager(Employee):
#     def __init__(self, name, age, salary , job):
#         super().__init__(name, age, salary)
#         self.job = job
#     def calculate_bonus(self):
#         print(f"Name:{self.name}, job:{self.job} ,  Bonus: {self.salary * 0.2}")
# def all_bonus(employees):
#     for i in employees:
#         i.calculate_bonus()
# employee1 = Developer("Abdallah" , 20 , 200000 , "Developer")
# employee2 = Manager("Rahma" , 20 , 200000 , "Manager")
# employees = [employee1 , employee2]
# all_bonus(employees)

        
# class Employee :
#     def __init__(self , name , salary):
#         self.name = name
#         self.__salary = salary
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self , salary):
#             if salary < 1000:
#                 print("Error salary")
#             else:
#                 self.__salary = salary
#     def display(self):
#         print(f"Name: {self.name} , Salary: {self.salary}")
# Employee1 = Employee("Abdallah", 50000)
# Employee1.display()


from developer import Developer
from designer import Designer

def all_salary(employees):
    for i in employees:
        print(f"Name: {i.name}, Salary: {i.calculate_salary()}")

employee1 = Developer("Abdallah", 100000)
employee2 = Designer("Rahma", 8000)
employees = [employee1, employee2]
all_salary(employees)
