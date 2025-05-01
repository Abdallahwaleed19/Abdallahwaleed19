class hotel : 
    def __init__(self , name ):
        self.name  = name 
    def room_availability(self):
        print(f"Room is available at {self.name}")
    def payment_processing(self):
        print(f"Payment is processed at {self.name}")
    def confirm_email(self):
        print(f"Email is sent from {self.name}")
    def loyalty_points(self):
        print(f"Loyalty points are added at {self.name}")
class Facade : 
    def __init__(self , name):
        self.hotel = hotel(name)
    def book_room(self):
        self.hotel.room_availability()
        self.hotel.payment_processing()
        self.hotel.confirm_email()
        self.hotel.loyalty_points()
facade = Facade("garnd plaza+++")
facade.book_room()