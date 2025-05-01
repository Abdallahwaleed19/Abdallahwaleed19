class Grinder : 
    def grind(self) :
        print("Grinding coffee beans...")
class Heater : 
    def heat(self) :
        print("Heating water...")
class Brewer : 
    def brew(self) :
        print("Brewing coffee...")
class Cup : 
    def pour(self) :
        print("Pouring coffee into cup...")
class Facade_Coffee_Maker :
    def __init__ (self):
        self.grinder = Grinder()
        self.heater = Heater()
        self.brewer = Brewer()
        self.cup = Cup()
    def make_coffee(self) :
        self.grinder.grind()
        self.heater.heat()
        self.brewer.brew()
        self.cup.pour()
Coffee_Maker = Facade_Coffee_Maker()
Coffee_Maker.make_coffee()