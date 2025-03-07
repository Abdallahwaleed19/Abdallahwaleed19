class Employee:
    # Class variable
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name


e1 = Employee("Alice")
e2 = Employee("Bob")

# Accessing class variable 
print(e1.company_name)  # Output: TechCorp
print(e2.company_name)  # Output: TechCorp

print(Employee.company_name)

# Key Point: Modifying a class variable through the class affects all instances
Employee.company_name = "NewTechCorp"
print(e1.company_name)  # Output: NewTechCorp
print(e2.company_name)  # Output: NewTechCorp

# but modifying it through an instance creates an instance-specific attribute.

e1.company_name = "Test"
print(e1.company_name)  # Output: Test
print(e2.company_name)  # Output: NewTechCorp
print(Employee.company_name)  # Output: NewTechCorp
















