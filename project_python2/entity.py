
class Entity:
    #Used to represent entities

    def __init__(self,x,y,char,color):
        self.x=x
        self.y=y
        self.char=char
        self.color=color

    def move(self, dx, dy):
        #moves entities
        self.x+=dx
        self.y+=dy
