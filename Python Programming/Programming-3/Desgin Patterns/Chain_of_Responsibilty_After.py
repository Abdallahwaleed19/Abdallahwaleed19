from abc import ABC, abstractmethod
class Handler(ABC):
    def __init__ (self) :
        self.next_handler = None
    def set_next (self , handler) :
        self.next_handler = handler
        return handler
    @abstractmethod
    def handle (self , expense) :
        pass
class SmallManager(Handler):
    def handle (self , expense) :
        if expense.amount <= 100 :
            print("small manager handles expenses up to 100")
        elif self.next_handler is not None :
            self.next_handler.handle(expense)
class MediumManager(Handler):
    def handle (self , expense) :
        if expense.amount <= 500 :
            print("medium manager handles expenses up to 500")
        elif self.next_handler is not None :
            self.next_handler.handle(expense)
class LargeManager(Handler):
    def handle (self , expense) :
        if expense.amount <= 1000 :
            print("large manager handles expenses up to 1000")
        elif self.next_handler is not None :
            self.next_handler.handle(expense)
class Director(Handler):
    def handle (self , expense) :
        if expense.amount > 1000 :
            print("director handles expenses over 1000")
        elif self.next_handler is not None :
            self.next_handler.handle(expense)
class Expense:
    def __init__ (self , amount) :
        self.amount = amount

juinor = SmallManager()
medium = MediumManager()
senior = LargeManager()
director = Director()

expense1 = Expense(50)
expense2 = Expense(200)
expense3 = Expense(600) 
expense4 = Expense(1500)

juinor.set_next(medium).set_next(senior).set_next(director)

juinor.handle(expense1)
juinor.handle(expense2)
juinor.handle(expense3)
juinor.handle(expense4)