#Origanal Code 

class sybsystem_A :
    def operation_a(self):
        print("A")
class sybsystem_B :
    def operation_b(self):
        print("B")
class sybsystem_C :
    def operation_c(self):
        print("C")


# Code in Facade 
class Facade :
    def __init__(self):
        self.a = sybsystem_A()
        self.b = sybsystem_B()
        self.c = sybsystem_C()

    def operation(self):
        self.a.operation_a()
        self.b.operation_b()
        self.c.operation_c()
facade = Facade()
facade.operation()