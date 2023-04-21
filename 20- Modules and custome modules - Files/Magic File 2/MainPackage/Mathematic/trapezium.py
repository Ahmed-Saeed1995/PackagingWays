import imp
import os

if __name__ == "__main__":
    print("Executed internally")
    path = os.getcwd()
else:
    print("Executed externally")
    path = os.getcwd() + "\MainPackage\Mathematic"


LoadedModule = imp.load_source("", path + "\GeneralShape.py")
Shape = LoadedModule.Shape


class Trapezoid(Shape):
    
    def __init__(self, name, side1, side2, base1, base2):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.base1 = base1
        self.base2 = base2

    def Area(self, height = 1):
        area = 1/2 * ( self.base1 + self.base2 ) * height
        print(f"The area of a {self.name} is {area}")
        return area

    def Perimeter(self):
        perimeter = self.base1 + self.base2 + self.side1 + self.side2
        print(f"The perimeter of a {self.name} is {perimeter} ")
        return perimeter

    def ShapeName(self):
        print(self.name)

trap = Trapezoid("trapezoid", 2, 4, 6, 8)
trap.Area(19)
trap.Perimeter()