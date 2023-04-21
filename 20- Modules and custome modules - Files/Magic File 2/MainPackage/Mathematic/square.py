
from importlib.machinery import SourceFileLoader
import os


if __name__ == "__main__":
    print("Executed internally")
    path = os.getcwd()
else:
    print("Executed externally")
    path = os.getcwd() + "\MainPackage\Mathematic"

LoadedModule = SourceFileLoader("", path + "\GeneralShape.py").load_module()

Shape = LoadedModule.Shape

class Square(Shape):
    
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def Area(self):
        area = self.side ** 2 
        print(f"The area of a {self.name} is {area}")
        return area

    def Perimeter(self):
        perimeter = 4 * self.side
        print(f"The perimeter of a {self.name} is {perimeter} ")
        return perimeter

    def ShapeName(self):
        print(self.name)