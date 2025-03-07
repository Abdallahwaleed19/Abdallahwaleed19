class Shape:
    def area(self):
        print("")
        # raise NotImplementedError("This method should be overridden by a subclass")
    def display(self):
        print("Hello")

# obj1 = Shape()
# obj1.area() # 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # def area(self): # Override to area method that exists in Parent Class (Shape)
    #     return 3.14 * self.radius * self.radius

    def display(self,x):
        print("")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)] # List of Objects

for shape in shapes:
    print("Area:", shape.area())
