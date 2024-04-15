class Cuboid:
    # we can define defalut value to constructor to achieve constructor overloading.
    def __init__(self,l=0,b=0,h=0):
        print(id(self));
        #inside constructor declaration and initialization will be variable
        self.length = l;
        self.breadth = b;
        self.height = h;

# we can not declare more then one constructor
#    def __init__(self,l,b):
#        pass


    def leadArea(self):
        #self keyword must be passed because of they represent declaration of variable.__
        return self.length*self.breadth;

    def total(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.length*self.height);

    def volume(self):
        print(id(self));
        return self.length*self.breadth*self.height;


cuboid = Cuboid(2,3,4);
print(cuboid.leadArea());
print(cuboid.total());
print(cuboid.volume());
print(id(cuboid));

c2 = Cuboid(1,4);
print(id(c2));
c2.volume();
