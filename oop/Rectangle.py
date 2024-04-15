
class Rectangle:

    #class level variable which are applicable for all the object
    count = 0;
    def __init__(self,l,b):
        self.length = l;
        self.breadth = b;
        Rectangle.count +=1;

    def perimeter(self):
        return 2*(self.length * self.breadth);

    def area(self):
        return self.length * self.breadth;

    @classmethod
    def printRect(cls):
        print(cls.count);

    @staticmethod
    def isSquare(len,br):
        return len == br;



rect = Rectangle(2,3);
print(rect.perimeter());
Rectangle.printRect();
r2 = Rectangle(2,2);
Rectangle.printRect();
#static method can be access throgh objectreference or class name.
print(r2.isSquare(2,2));
print(Rectangle.isSquare(5,5));
