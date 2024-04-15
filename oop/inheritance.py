class Rectangle:
    def __init__(self,l,b):
        self.length = l;
        self.breadth = b;

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height = h;
        #calling parent constructor.
        super().__init__(l,b);

    def volume(self):
        return 2*(self.length * self.breadth * self.height);


cuboid = Cuboid(5,4,3);
print(cuboid.volume());
