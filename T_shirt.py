class T_shirt :
    def __init__(self,model,price):
        self.model = model
        self.price = price
    def __str__(self):
        return f"The model of t_shirt : {self.model} and his price : {self.price}"
    def __repr__(self):
        return f"The model of T_shirt : {self.model} and his price : {self.price}"
    def __eq__(self,other):
        return self.price == other.price
    def __lt__(self,other):
        return self.price < other.price
    def __le__(self,other):
        return self.price <= other.price
    def __gt__(self,other):
        return self.price > other.price 
    def __ge__(self,other):
        return self.price >= other.price 
    def __add__(self,other):
        return T_shirt(self.model + " & " + other.model , self.price + other.price )
    def __sub__(self,other):
        return T_shirt(self.model + " - " + other.model , self.price - other.price )
    def __del__(self):
        print ("The object is deleted")
    
    
T1 = T_shirt("PoLo T_shirt " , 5000 )
T2 = T_shirt("Adidas T_shirt " , 3000 )
print(str(T1))    
print(repr(T2))
print(T1 == T2 ) 
print(T1 < T2 )
print(T1 <= T2 )
print(T1 > T2 )
print(T1 >= T2 )
print(T1+T2)
print(T1-T2)
del T1









