from abc import ABC, abstractmethod
class SupportRequest:
    def __init__(self, level, description):
        self.level = level  
        self.description = description
class SupportHandler(ABC):
    def __init__ (self) :
        self.next_handler = None 
    def set_next (self , handler) :
        self.next_handler = handler
        return handler
    @abstractmethod
    def handler (self , request) :
        pass 
class FirstLevelSupport(SupportHandler):
    def handler (self , request) :
        if request.level == 1:
            print("The request is being handled by the first level support team")
        elif self.next_handler:
            self.next_handler.handler(request)
class SecondLevelSupport(SupportHandler):
    def handler (self , request) :
        if request.level == 2:
            print("The request is being handled by the second level support team")
        elif self.next_handler:
            self.next_handler.handler(request)
class ThirdLevelSupport(SupportHandler):
    def handler (self , request) :
        if request.level == 3:
            print("The request is being handled by the third level support team")
        elif self.next_handler:
            self.next_handler.handler(request)
class UnknownLevelSupport(SupportHandler):
    def handler (self , request) :
        print("The request cannot be handled by any support team")

first_level_support = FirstLevelSupport()
second_level_support = SecondLevelSupport()
third_level_support = ThirdLevelSupport()
unknown_level_support = UnknownLevelSupport()

first_level_support.set_next(second_level_support).set_next(third_level_support).set_next(unknown_level_support)

requests = [
    SupportRequest(1, "problem with login"),
    SupportRequest(2, "server connection issue"),
    SupportRequest(3, "technical support needed"),
    SupportRequest(4, "unknown issue"),
]

for request in requests:
    first_level_support.handler(request)