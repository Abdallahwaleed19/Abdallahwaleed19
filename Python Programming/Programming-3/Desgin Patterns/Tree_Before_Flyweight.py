class Tree : 
    def __init__ (self , x , y , color , type , texture):
        self . x = x
        self . y = y
        self . color = color
        self . type = type
        self . texture = texture
    def draw (self , canvas):
        print (f"Drawing a {self . color} {self . type} , {self.texture} ,  tree at ({self . x}, {self . y}) on {canvas} canvas")
forest = []
for i in range (1000):
    forest . append (Tree (i , i , "green" , "oak" , "rough"))
for i in range (1000):
    forest . append (Tree (i , i , "green" , "pine" , "smooth"))
    
print (f"Forest has {len(forest)} trees")
   