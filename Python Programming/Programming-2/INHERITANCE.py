# region 1- Basic Inheritance
"""
Inheritance allows a class (called the child class or subclass) to inherit attributes and methods from another class (called the parent class or superclass). 
It helps promote code reuse, as the child class can use the code from the parent class without having to rewrite it.
The child class can also have its own methods or override methods from the parent class.
"""
# Parent class Animal
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the animal's name
    
    def make_sound(self):
        print(f"{self.name} makes a sound.")  # Method common to all animals

# # Child class Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed      # Additional attribute for Dog class

    def make_sound(self):
        print(f"{self.name} barks!")  # Overriding the make_sound method for Dog

# Creating an object of the Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.make_sound()
print(dog)
print(dog.breed)
# # Calling methods
# dog.make_sound()  # Output: Buddy barks!
# print(dog.breed)  # Output: Golden Retriever
#endregion

# region 2- Method Overriding and Adding New Methods
# Parent class Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# # Child class Student inherits from Person
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)  # Call parent class constructor
#         self.student_id = student_id  # Additional attribute for Student
    
#     def introduce(self):
#         # Overriding the introduce method
#         print(f"My name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")
    
#     def study(self):
#         print(f"{self.name} is studying.")

# # Creating an object of the Student class
# student = Student("John", 21, "S12345")

# # Calling methods
# student.introduce()  # Output: My name is John, I am 21 years old, and my student ID is S12345.
# student.study()      # Output: John is studying.
#endregion

# region 3- Multilevel Inheritance
# Base class Bird
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

# Derived class Parrot inherits from Bird
class Parrot(Bird):
    def repeat_words(self):
        print(f"{self.name} is repeating words!")

# Derived class TalkingParrot inherits from Parrot
class TalkingParrot(Parrot):
    def talk(self):
        print(f"{self.name} is talking!")

# Creating an object of the TalkingParrot class
parrot = TalkingParrot("Polly")

# Calling methods from all levels of inheritance
parrot.fly()           # Output: Polly is flying.
parrot.repeat_words()   # Output: Polly is repeating words!
parrot.talk()           # Output: Polly is talking!
#endregion

# region 4- Multiple Inheritance
# Parent class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Parent class 2
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def work(self):
        print(f"Employee {self.employee_id} is working as a {self.position}.")

# Child class inherits from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        # Initialize attributes from both parent classes
        Person.__init__(self,name, age)
        Employee.__init__(self,employee_id, position)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing the {self.department} department.")

# Creating an object of the Manager class
manager = Manager("Alice", 35, "M123", "Manager", "Sales")

# Calling methods from both parent classes and the child class
manager.introduce()    # Output: My name is Alice and I am 35 years old.
manager.work()         # Output: Employee M123 is working as a Manager.
manager.manage()       # Output: Alice is managing the Sales department.
#endregion

