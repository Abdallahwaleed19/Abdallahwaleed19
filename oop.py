class dog :
    dog_count=0
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        dog.dog_count +=1 
        print("Welcome My Dog ")
    def dogcount(self):
        return f"Total of dogs is = {dog.dog_count}"
    def sit(self):
        return f"{self.name} is {self.age} , and it is sitting "
    def roll_over(self):
        return f"{self.name} is {self.age} , and it is rolled over "
dog1=dog("Roy",10)
dog2=dog("Tom",9)
dog3=dog("Jerry",5)  
print(dog1.sit(),dog1.roll_over())    
print(dog2.sit(),dog2.roll_over())    
print(dog3.sit(),dog3.roll_over())   
print(dog1.dogcount())




print("----------------------------------------------------------------------------------")




class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount +=1
        print(f"The employee {self.name} is created ") 
    def displaycount(self):
        return f" Total employee = {Employee.empcount} "  
    def displayemployee(self):
        return f" Name is : {self.name} and his salary is : {self.salary}" 
emp1= Employee("Abdallah",100000)
emp2= Employee("Saif",40000)
emp3= Employee("Ali",50000)  
print(emp1.displayemployee()) 
print(emp2.displayemployee()) 
print(emp3.displayemployee())
print(emp1.displaycount())




print("----------------------------------------------------------------------------------")




class Hello :
    Names_count=0
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender 
        Hello.Names_count+=1
        print(" Welcome to my account ")
    def displaynamescount(self):
        return f"The total names is = {Hello.Names_count}"    
    def kind (self):
        if (Hello =="Male"):
            return f"{self.name} is {self.age} , and he is {self.gender}"
        else:
             return f"{self.name} is {self.age} , and she is {self.gender}"
person1= Hello ("Abdallah",19,"Male") 
person2= Hello ("Mona",20,"Female")
person3= Hello ("Rana",21,"Female")
person4= Hello ("Ahmed",22,"Male")
print(person1.kind())
print(person2.kind())
print(person3.kind())
print(person4.kind())
print(person1.displaynamescount())



print("----------------------------------------------------------------------------------")




class parent :
    parentAttr = 100
    def __init__(self) :
        print("Call parent class construction method ")
    def parentMethod (self):
        print("Call parent class method ")
    def setAttr(self,attr):
        parent.parentAttr = attr
    def getAttr(self):
        print("Parent class attribute = " , parent.parentAttr)        
class child (parent):
    def __init__(self):
        super().__init__()
        print("Call sub-class construction method ")
    def childMethod(self):
        print("Call sub-class method ")
c = child()
c.childMethod()
c.parentMethod() 
c.getAttr()
c.setAttr(200)      
c.getAttr()




print("----------------------------------------------------------------------------------")





