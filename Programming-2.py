# def add_numbers(x: int, y: int) -> int:
#     """
#     This function adds two numbers together.
#     """
#     return x + y
# print(add_numbers(1,2))



# def calculate_result(a,b,c):
#     result = 0
#     for i in range (a):
#         if i % 2 == 0 :
#             result += i * b
#         else:
#             result += i * c
#     return result
# print(calculate_result(1,2,3))            



# class A:
#    def __init__(self):
#       self.count=5
#       self.count= self.count + 1
# a= A()
# print(a.count)




# class Connector :
#     def __init__(self,source):
#         self.source = source 
#         self.__timeout = 60
#     def connect (self):
#         print("connecting with{0}s".format(self.__timeout))    



# class Parent : 
#     def __init__(self):
#         self.__private_var = "Parent is private variable "
#     def get_private_var (self):
#         return self.__private_var
# class Child (Parent):
#     def __init__(self):
#         super().__init__()
#         self.__private_var = "Child is private variable "
# parent = Parent()
# child = Child()
# print(parent.get_private_var())
# print(child.get_private_var())



# class Circle :
#     def __init__(self,radius):
#         self.radius = radius
#     @property
#     def area (self):
#         return 3.14 * self.radius ** 2
#     @area.setter
#     def area (self,value):
#         if value < 0 :
#             raise ValueError ("Area cannot be Negative")
#         self.radius = (value/3.14)** 0.5
# c = Circle(2)
# print(c.area)
# c.area = 50
# print(c.radius)            
# c.area = -10 
# print(c.radius)



# class coordinate :
#     def __init__(self,lat: float , long : float) -> None :
#         self._latitude  = self._longitude  = None 
#         self.latitude  = lat 
#         self.longitude = long 
#     @property
#     def latitude (self) ->float :
#         return self._latitude
#     @latitude.setter
#     def latitude (self,lat_value : float ) -> None :
#         if lat_value not in range (-90 , 90+1):
#             raise ValueError (f"{lat_value} is an invalid value for latitude ")
#         self._latitude = lat_value
#     @property
#     def longitude (self)  -> float :
#         return self._longitude
#     @longitude.setter
#     def longitude (self, long_value : float ) -> None :
#         if long_value not in range (-180 , 180+1):
#             raise ValueError (f"{long_value} is invalid value for longitude ")
#         self._longitude = long_value       
        

# class Person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#     def __repr__(self):
#         return f"person (name='{self.name}'),age={self.age}"
# person = Person("Abdallah",20)
# print(person.__repr__())        



# list = [1,2,3,4,5]
# for i in list :
#     print (i)
    
# my_iterator = iter(list)
# while True :
#     try:
#         item = next (my_iterator)
#         print(item)
#     except StopIteration :
#         break    


# def regtangle_area (width,height):
#     return width * height
# area = regtangle_area(5,2)
# print(area)



# class animal :
#     def __init__(self,name,voice):
#         self.name = name 
#         self.voice  = voice
#     def getanimal (self):
#         return f"The animal name is {self.name} and his voice is {self.voice}"
# class dog (animal):
#     def __init__(self, name, voice,colour):
#         super().__init__(name, voice)
#         self.colour  = colour
#     def getanimal(self):
#         return f"The Dog name is {self.name} and his voice is {self.voice} and his colour is {self.colour}"
# dog1 = dog("Tom","Bark","Black")
# print(dog1.getanimal())                



# class Libraryitem:
#     def __init__(self, Title, author, publication_year):
#         self.Title = Title
#         self.author = author
#         self.publication_year = publication_year

# class Book(Libraryitem):
#     def __init__(self, Title, author, publication_year, ISBN):
#         super().__init__(Title, author, publication_year)
#         self.ISBN = ISBN

#     @property
#     def display_info(self):
#         if self.publication_year < 0 or self.ISBN < 0:
#             return "Invalid"
#         else:
#             return f"{self.Title}, {self.author}, {self.publication_year}, {self.ISBN}"

# class Magazine(Libraryitem):
#     def __init__(self, Title, author, publication_year, Issue):
#         super().__init__(Title, author, publication_year)
#         self.Issue = Issue

#     @property
#     def display_info(self):
#         if self.publication_year < 0 or self.Issue < 0:
#             return "Invalid"
#         else:
#             return f"{self.Title}, {self.author}, {self.publication_year}, {self.Issue}"

# Book1 = Book("Animal", "Ahmed", 2024, 1234)
# Magazine1 = Magazine("Elmasry Elyom", "Mohamed", 2020, 5678)

# print(Book1.display_info)
# print(Magazine1.display_info)
        
                                        