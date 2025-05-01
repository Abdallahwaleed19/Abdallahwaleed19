class Character : 
    def __init__ (self , char , font , color , size):
        self.char = char
        self.font = font
        self.color = color
        self.size = size
    def render (self , x , y):
        print (f"Rendering {self.char} at ({x}, {y}) with font {self.font}, color {self.color}, size {self.size}")
text  = []
for char in "Hello World":
    text.append(Character(char, "Arial", "black", 12))
print("Before Flyweight:")
for char in text:
    char.render(0, 0)