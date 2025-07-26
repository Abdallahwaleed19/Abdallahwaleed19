from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_salary(self):
        pass
