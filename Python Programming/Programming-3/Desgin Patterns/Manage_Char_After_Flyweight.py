class Char_Style:
    def __init__(self, font, color, size):
        self.font = font
        self.color = color
        self.size = size

    def render(self, x, y, char):
        print(f"Rendering {char} at ({x}, {y}) with font {self.font}, color {self.color}, size {self.size}")


class Char_factory:
    _style_char = {}
    @classmethod
    def get_char_style(cls, font, color, size):
        key = (font, color, size)  
        if key not in cls._style_char:
            cls._style_char[key] = Char_Style(font, color, size)
        return cls._style_char[key]


class Char:
    def __init__(self, char, font, color, size):
        self.char = char
        self.style = Char_factory.get_char_style(font, color, size)

    def render(self, x, y):
        self.style.render(x, y, self.char)


text = []
for char in "Hello World":
    text.append(Char(char, "Arial", "black", 12))
print("After Flyweight:")
for i, char in enumerate(text):
    char.render(i, 0)