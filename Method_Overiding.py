class shapes:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Area(self):
        return self.x * self.y    

class circle(shapes):
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius

rectangle = shapes(3, 5)
print(rectangle.Area())  

c = circle(5)
print(c.Area())