# region 1- Why needing OOP !
"""
Primitive data structures—like numbers, strings, 
and lists—are designed to represent straightforward pieces of information, 
such as the cost of an apple, the name of a poem, or your favorite colors, 
respectively. What if you want to represent something more complex?

For example, you might want to track employees in an organization. 
You need to store some basic information about each employee, 
such as their name, age, position, and the year they started working.

One way to do this is to represent each employee as a list:

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

There are a number of issues with this approach.

First, it can make larger code files more difficult to manage. 
If you reference kirk[0] several lines away from where you declared the kirk list,
 will you remember that the element with index 0 is the employee’s name?

Second, it can introduce errors if employees don’t have the same number of elements in their respective lists. 
In the mccoy list above, the age is missing, 
so mccoy[1] will return "Chief Medical Officer" instead of Dr. McCoy’s age.
"""
#endregion

# region 2- Defining a Class
# Defining a class called Car

class Car:
    # Constructor method to initialize a new object
    def __init__(self, brand, model, year):
        # Initializing object attributes
        self.brand = brand  # Brand of the car
        self.model = model  # Model of the car
        self.year = year    # Year of manufacture
    # Method to display car information
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    # Method to start the engine
    def start_engine(self):
        print(f"{self.model} engine started.")

# Creating an object of the Car class

my_car = Car("Toyota", "Corolla", 2020)
#my_car = Car("Toyota", "Corolla", 2020)

# Calling the method to display car details
my_car.display_info()  # Output: Brand: Toyota, Model: Corolla, Year: 2020

# Calling the method to start the engine
my_car.start_engine()  # Output: Corolla engine started.


# # Defining a class called Person
class Person:
    # Constructor method to initialize attributes when creating a new object
    def __init__(self, name, age, city):
        self.name = name  # Person's name
        self.age = age    # Person's age
        self.city = city  # Person's city

    # Method to display person's information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

    # Method to update the person's age
    def update_age(self, new_age):
        if new_age > 0:  # Checking if the new age is valid
            self.age = new_age
            print(f"Age updated to {self.age}")
        else:
            print("Invalid age!")

# Creating an object of the Person class
person1 = Person("Alice", 25, "New York")

# Calling the method to display the person's details
person1.display_info()  # Output: Name: Alice, Age: 25, City: New York

# Updating the person's age and displaying the updated info
person1.update_age(26)  # Output: Age updated to 26
person1.display_info()  # Output: Name: Alice, Age: 26, City: New York

#endregion

# region 3- Class Attributes, Instance Attributes and Local Attributes
class Counter:
    def __init__(self):
        self.count = 0  # Instance variable

    def increase(self):
        count = 10  # Local variable
        self.count += 1  # Incrementing instance variable `self.count`
        print(f"Local count: {count}, Instance count: {self.count}")

counter = Counter()
counter.increase()  # Output: Local count: 10, Instance count: 1


class Employee():
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        print("The employee",self.name,"is created")
    # def increase_empcount(self):
    #     Employee.empCount+=1
    # def displayCount(self):
    #     print("Total Employee %d" % Employee.empCount )
    def displayEmployee(self):
        print("Name: ", self.name,  ", Salary: ", self.salary)

emp1 = Employee('Ali',5000)
emp2 = Employee('Ahmed',40000)
emp3 = Employee("Manni", 5000)
emp4 = Employee("Alibaba", 330)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()

print(f"Total Employees: {Employee.empCount}")
# # print("Total Employee %d" % Employee.empCount)

#endregion