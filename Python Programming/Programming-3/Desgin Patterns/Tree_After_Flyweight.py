class Tree_type :
    def __init__ (self , color , type , texture):
        self . color = color
        self . type = type
        self . texture = texture
    def draw (self , x , y , canvas):
        print (f"Drawing a {self . color} {self . type} , {self.texture} , tree at ({x}, {y}) on {canvas} canvas")
class Tree_factory :
    _tree_types = {}
    @classmethod
    def get_tree_type (cls , color , type , texture):
        key = (color , type , texture)
        if key not in cls . _tree_types:
            cls . _tree_types [key] = Tree_type (color , type , texture)
        return cls . _tree_types [key]
class Tree :
    def __init__ (self , x , y , color , type , texture):
        self . x = x
        self . y = y
        self . tree_type = Tree_factory . get_tree_type (color , type , texture)
    def draw (self , canvas):
        self . tree_type . draw (self . x , self . y , canvas)
forest = []
for i in range (1000):
    forest . append (Tree (i , i , "green" , "oak" , "rough"))
print (f"Forest has {len(forest)} trees")
