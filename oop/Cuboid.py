class Cuboid:
    def __init__(self,l,b,h):
        #inside constructor declaration and initialization will be variable
        self.length = l;
        self.breadth = b;
        self.height = h;

    def leadArea(self):
        #self keyword must be passed because of they represent declaration of variable.
        return self.length*self.breadth;

    def total(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.length*self.height);

    def volume(self):
        return self.length*self.breadth*self.height;


cuboid = Cuboid(2,3,4);
print(cuboid.leadArea());
print(cuboid.total());
print(cuboid.volume());
