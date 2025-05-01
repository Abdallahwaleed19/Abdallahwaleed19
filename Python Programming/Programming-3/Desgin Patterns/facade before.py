class Hotel:
    def __init__(self, name):
        self.name = name

    def room_availability(self):
        print(f"Room is available at {self.name}")

    def payment_processing(self):
        print(f"Payment is processed at {self.name}")

    def confirm_email(self):
        print(f"Email is sent from {self.name}")

    def loyalty_points(self):
        print(f"Loyalty points are added at {self.name}")

hotel = Hotel("Grand Plaza")
hotel.room_availability()
hotel.payment_processing()
hotel.confirm_email()
hotel.loyalty_points()