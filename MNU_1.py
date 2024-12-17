#def twice ( y,x ):
    #return y(y(x))
#def mul (x):
   # return x**2
#out = twice (mul , 2)
#print(out)



# def function1 (x):
#    def function2 (y):
#       return y+2
#    return 3 * function2(x)
# a= function1(2)
# print(a)
# b=function1(2.5)
# print(b)



# length = 4.2 
# height = 3.5 
# area = length * height
# prim = 2* (length+height)
# print(area,prim)




# Trafic_light = input()
# if (Trafic_light == "Green"):
#     print("DRIVE")
# elif(Trafic_light == "Yellow"):
#     print("ACCELRATE")
# else:
#     print("STOP")        





# def Hello_World ():
#     print("Hello world")
# def Hello_name (name):
#     return f"Hello,{name}"
# print(Hello_name("Abdallah"))
# Hello_World()   



# def function1(x):
#     def function2(y):
#         print(y+2)
#         return y+2
#     return 3* function2(x)
# a= function1(2)
# print(a)
# b= function1(2.5)
# print(b)



# def f1():
#     global x
#     x=x+1
#     return x
# def f2():
#     return x
# def f3():
#     x=5
#     return x+1
# x=0
# print(f1())
# print(f2())
# print(f3())





# def loop ():
#     for x in range (10):
#         print(x)
#         if x == 3:
#             return x
# loop() 


# x = 1
# def add_one (x):
#     x = x+1
#     return x
# y = add_one(x)
# print (x,y)



# x = 0
# def incr_x():
#     x = x+1 
# def incr_x2():
#     global x
#     x = x+1
#     return x
# print(incr_x2())        



# A = [1,2,3,4]
# B = A
# C = list(A)
# print(id(A))
# print(id(B))
# print(id(C))



# class Employee () :
#     def __init__(self,name,age,salary,email):
#         self.name = name
#         self.age = age 
#         self.salary = salary
#         self.email = email
#     def Employee_info(self):
#         print (f"The Employee Info : Name : {self.name}, Age : {self.age}, Salary : {self.salary}, Email : {self.email}")  
# Em1 = Employee("Abdallah Waleed",20,1000000,"Waleedabdallah@gmail.com")
# Em1.Employee_info()  
# print(id(Em1))   
# print(Em1)     




# class student :
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age 
#     def __str__(self):
#         return f"The student name : {self.name} and his age : {self.age}"
#     def __repr__(self):
#         return f"The student name : {self.name} and his age : {self.age}"
#     def __eq__(self,other):
#         return self.age == other.age
#     def __lt__(self,other):
#         return self.age < other.age 
#     def __le__(self,other):
#         return self.age <= other.age 
#     def __gt__(self,other):
#         return self.age > other.age 
#     def __ge__(self,other):
#         return self.age >= other.age 
#     def __add__(self,other):
#         return student(self.name +"&"+ other.name , self.age + other.age)
#     def __sub__(self,other):
#         return student(self.name + "-" + other.name , self.age - other.age )
    
    
# s1 = student("Abdallah" , 20 )
# s2 = student("Rahma" , 19 )
# print(str(s1))    
# print(repr(s2))
# print(s1 == s2 ) 
# print(s1 < s2 )
# print(s1 <= s2 )
# print(s1 > s2 )
# print(s1 >= s2 )
# print(s1 + s2 )
# print(s1 - s2 )






# class animal :
#     def speak (self):
#         pass 
# class cat (animal):
#     def __init__(self,sound):
#         self.sound = sound
#     def speak(self):
#         print(self.sound)
# class dog (animal):
#     def __init__(self, sound):
#         self.sound = sound
#     def speak(self):
#         print (self.sound)
# class cow (animal):
#     def __init__(self,sound):
#         self.sound = sound 
#     def speak(self):
#         print (self.sound)           
# list_of_sounds = [cat("Meao") , dog("HaoHao") , cow("MMMMMMMMMMM")] 
# def sounds (list_of_sounds):
#     for sound in list_of_sounds :
#          sound.speak()
# sounds(list_of_sounds)      

# class Person :
#     def __init__(self,name,age):
#         self.name = name 
#         self.age  = age 
#     def getname (self):
#         return f"The person name is {self.name}"
#     def getage (self):
#         return f"{self.name} age is {self.age}"
# class Child1(Person):
#     def __init__(self, name, age , weight):
#         self.weight = weight
#         super().__init__(name, age)
        
#     def getweight(self):
#         return f"{self.name} his weight is {self.weight}"

# p1 = Person("Abdallah",20)  
# p2 = Child1("Ali" , 22, 72)  
# print(p1.getname())
# print(p1.getage())
# print(p2.getname())
# print(p2.getage())
# print(p2.getweight())




# class grandfather :
#     def __init__(self,name):
#         self.name = name 
#     def getname (self):
#         return f"The grand father name is {self.name}"
# class father(grandfather) :
#     def __init__(self,name,age):
#         grandfather.__init__(self,name)
#         self.age = age 
#     def getage (self):
#         return f"The father name is {self.name} and his age is {self.age}"
# class son (father):
#     def __init__(self, name, age,address):
#         father.__init__(self,name, age)
#         self.address = address
#     def getaddress (self):
#         return f"The son name is {self.name},and his age is {self.age} and his address is {self.address}"
# grandfather1 = grandfather("Kamal")
# father1 = father("Waleed", 45)
# son1 = son("Abdallah",20,"Shibin elkom")
# print(grandfather1.getname())
# print(father1.getage())
# print(son1.getaddress())   







# class person :
#     def __init__(self,id,name):
#         self._id = id
#         self._name = name 
#     def display(self):
#         return f"the name is {self._name} and his id is {self._id}"
# person1 = person(20230192,"Abdallah")
# print(person1.display())      #not clean code 
                               





# class person : 
#     def __init__(self,name):
#         self.name = name 
#     def get_name (self):
#         return self.name 
# cond = True
# class son (person if cond else object ):
#     def isperson(self):
#         return True
# person1  = son(1)
# print(person1.isperson())            
                               




# class University :
#     name_University = "Menoufia National University"
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
# A = University("Menoufia","Shibin elkom")
# B = University("Cairo","Cairo")
# print(A.name_University)        
# print(B.name_University)  
# print(A.name)
# print(A.address)
# print(B.name)
# print(B.address)             



# class Student :
#     student_name  = "Abdallah waleed"
#     def __init__(self,name):
#         self.name = name 
# st1 = Student("saif")    
# st2 = Student("Ahmed")
# print(st1.student_name) 
# print(st2.student_name)
# print(Student.student_name)
# Student.student_name = "Rahma"
# print(st1.student_name)
# print(st2.student_name)
# st1.student_name = "Jana"
# print(st1.student_name)
# print(st2.student_name)
# print(Student.student_name)
# print(st1.name)




# class animal :
#     def voice (self):
#         print("The dog voice is Bark ")
# class cat (animal):
#     def voice (self):
#         super().voice()
#         print("The cat voice is MEO")     
# c1 = cat()
# print(c1.voice())         



# def Result (Number1,Number2):
#     result = Number1 + Number2
#     return result
# print(Result(5,7))

# def Result (Number1 , Number2 , Number3)    :
#     result = Number1 + Number2 + Number3
#     return result

# print(Result(5,7,8))    



# def add (datatype , *args):
#     if datatype == "int":
#         result = 0
#     if datatype == "str":
#         result = "" 
#     for i in args :
#         result = result + i
#     return result    
# print(add ("int",4,5))
# print(add ("int",4,5,6,7))
# print(add ("str","Abdallah","Waleed"))


# from abc import ABC , abstractmethod
# class shape (ABC):
#     @abstractmethod
#     def area (self):
#         pass 
#     @abstractmethod
#     def primiter (self):
#         pass 
# class square (shape):
#     def __init__(self,value):
#         self.value = value
#     def area(self):
#         return self.value **2
#     def primiter(self):
#         return self.value * 4
# square1 =  square(5) 
# print(square1.area())
# print(square1.primiter())   
            


# class car :
#     def __init__(self,brand , year):
#         self.brand = brand
#         self.year = year
#     def move (self):
#         return f"{self.brand} and {self.year} is Drive!"
# class Boat :
#     def __init__(self,brand , year):
#         self.brand = brand 
#         self.year = year 
#     def move (self):
#         return f"{self.brand} and {self.year} is sail!"
# car1 = car("Toyota" , 2020)
# boat1 = Boat("Titanic" , 1988)                    
# list = [car1 , boat1]
# for i in list :
#     i.move()
#     print(i.move())




# def Hello (name):
#     """
#     to great some one when you meet him  """
    
#     return f"Hello {name}"
# print(Hello.__doc__)
# print(Hello("Ahmed"))



# list = [1,2,3,4,5]
# iterator = iter(list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# def infinete_numbers():
#     n=1
#     while True :
#         yield n 
#         n += 1
# numbers  = infinete_numbers()
# print(next(numbers))
# print(next(numbers))        


# class circle :
#     def __init__(self,radius):
#         self._radius  = radius
#     @property
#     def radius (self):
#         return self._radius
#     @radius.setter
#     def radius (self, value):
#         if value < 0 :
#             raise ValueError("Error")
#         self._radius = value
#     @radius.deleter
#     def radius (self , value ):
#         self._radius = 0
#     @property
#     def area (self):
#         return 3.14 * (self._radius ** 2)        
    
# circle1 = circle(5)      
# print(circle1.radius)
# print(circle1.area)  




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.front = self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Circular link
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular link
        self.length -= 1
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:  # Circular condition
                break
        print()

# Example usage
myQueue = CircularQueue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ")
myQueue.printQueue()
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
print("Queue after operations: ")
myQueue.printQueue()






    
    
    