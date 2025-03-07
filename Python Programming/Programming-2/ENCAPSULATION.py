# region 1- Defenition
"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed by an object’s method.
Those types of variables are known as private variables.
Consider a real-life example of encapsulation, in a company, 
there are different sections like the accounts section, finance section, sales section etc. 
The finance section handles all the financial transactions and keeps records of all the data related to finance. 
Similarly, the sales section handles all the sales-related activities and keeps records of all the sales. 
Now there may arise a situation when due to some reason an official from the finance section needs all the data about sales in a particular month. In this case, 
he is not allowed to directly access the data of the sales section. He will first have to contact some other officer in the sales section and then request him to give the particular data. 
This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”. 
Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""
#endregion

#region 2- Protected Members
"""
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
"""

# Python program to
# demonstrate protected members

# Creating a base class
# class Base:
#     def __init__(self):

#         # Protected member
#         self._a = 2

# # Creating a derived class
# class Child(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ", 
#               self._a)

#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ",
#               self._a)


# obj2 = Child()
# # Accessing the protected variable outside

# print("Accessing protected member of obj2: ", obj2._a) # Not Allowed to call _a frm here

#endregion

#region 3- Private Members
"""
Private members are similar to protected members, 
the difference is that the class members declared private should neither be accessed outside the class nor by any base class.
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
However, to define a private member prefix the member name with double underscore “__”.
"""
# Python program to
# demonstrate private members

# Creating a Base class


# class Base:
#     def __init__(self):
#         self._a = "GeeksforGeeks - Protected"
#         self.__c = "GeeksforGeeks - Private"

# # Creating a derived class
# class Child(Base):
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         # print(self.__c)

# obj2=Child()
# print(obj2._a)
# print(obj2.__c)
#endregion

#region 4- Examples
# 1-
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number   # Public attribute
#         self.__balance = balance               # Private attribute (hidden)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Insufficient balance or invalid amount.")

#     def get_balance(self):
#         return self.__balance

# # # # # # Using the BankAccount class
# account = BankAccount("123456789", 1000)
# print("Balance Before Any Deposit or Withdraw:",account.get_balance())
# account.deposit(500)
# account.withdraw(200)
# account.__balance = 50000
# # # # # print(account.__balance)
# print("Current Balance:", account.get_balance())

# 2- 
class Employee:
    def __init__(self, name, job_title):
        self.name = name               # Public attribute
        self.job_title = job_title      # Job title provided by the user
        self.__base_salary = self.calculate_base_salary()  # Private, auto-determined base salary
        self.__bonus = 0                # Private, initial bonus set to 0

    # Automatically calculate base salary based on job title
    def calculate_base_salary(self):
        # Base salary is determined by job title
        salary_table = {
            "Junior Developer": 3000,
            "Senior Developer": 5000,
            "Manager": 7000,
            "Director": 10000
        }
        return salary_table.get(self.job_title, 3000)  # Default salary if title not found

    # Getter for base salary
    @property      
    def get_base_salary(self):
        return self.__base_salary
    
    def get_bonus(self):
        return self.__bonus
    
    # Setter for bonus with validation
    def set_bonus(self, amount):
        if 0 <= amount <= 0.2 * self.__base_salary:  # Bonus cannot exceed 20% of base salary
            self.__bonus = amount
            print(f"Bonus updated to: {self.__bonus}")
        else:
            print("Invalid bonus amount. Must be between 0 and 20% of base salary.")

    # Method to calculate total salary
    def calculate_total_salary(self):
        return self.__base_salary + self.__bonus

    # Display employee info
    def display_employee_info(self):
        print(f"Employee: {self.name}")
        print(f"Job Title: {self.job_title}")
        print(f"Base Salary: {self.__base_salary}")
        print(f"Bonus: {self.__bonus}")
        print(f"Total Salary: {self.calculate_total_salary()}")

# # # Create an employee with a name and job title
employee = Employee("Alice", "Senior Developer")
# employee.__bonus = 1000 # Not Allowed
# # # Set a bonus
# employee.set_bonus(1000)  # Should be valid if within 20% of base salary

employee._Employee__bonus = 20000
# # # Display employee info
employee.display_employee_info()
# print("Base Salary:",employee.get_base_salary)
# print("Base Salary:",employee.get_base_salary()) 
# print("Bonus Salary:",employee.get_bonus()) 
#endregion