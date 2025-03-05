class car ():
    def __init__(self,model,price):
        self.model = model 
        self.price = price 
    def display (self):
        return f"the car is {self.model},and this price is {self.price}"
class truck (car):
    def __init__(self, model, price,size):
        car.__init__(self,model,price)
        self.size = size 
    def display(self):
        return f"The truck is {self.model},and this price is {self.price},and size is {self.size}"
car1 =  car("sisi","10000000")
truck1 = truck("entisar","1000000000000","100 TON") 
print(car1.display())
print(truck1.display())    



print("--------------------------------------------------------------------------------------------------------")



        