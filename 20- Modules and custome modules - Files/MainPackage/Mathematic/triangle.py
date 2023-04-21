
import importlib
import os


if __name__ == "__main__":
    print("Executed internally")
    path = os.getcwd()
else:
    print("Executed externally")
    path = os.getcwd() + "\MainPackage\Mathematic"

LoadedModule = importlib.import_module("MainPackage.Mathematic.GeneralShape")

Shape = LoadedModule.Shape

class Triangle(Shape):
    
    def __init__(self, name, side1, side2, base):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.base = base

    def Area(self, height = 1):
        area = 1/2 * self.base * height
        print(f"The area of a {self.name} is {area}")
        return area

    def Perimeter(self):
        perimeter = self.side1 + self.side2 + self.base
        print(f"The perimeter of a {self.name} is {perimeter} ")
        return perimeter

    def ShapeName(self):
        print(self.name)