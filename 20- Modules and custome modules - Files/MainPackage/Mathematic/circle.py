import importlib.util
import os


if __name__ == "__main__":
    print("Executed from circle module")
    path = os.getcwd()
else:
    print("Executed externally")
    path = os.getcwd() + "\MainPackage\Mathematic"

spec = importlib.util.spec_from_file_location("", path + "\GeneralShape.py" )
GeneralShape = importlib.util.module_from_spec(spec)
spec.loader.exec_module(GeneralShape)

Shape = GeneralShape.Shape

class Circle(Shape):
    
    def __init__(self, name, raduis):
        super().__init__(name)
        self.raduis = raduis

    def Area(self):
        area = 3.14 * self.raduis **2
        print(f"The area of a {self.name} is {area}")
        return area

    def Perimeter(self):
        perimeter = 2 * self.raduis * 3.14
        print(f"The perimeter of a {self.name} is {perimeter} ")
        return perimeter

    def ShapeName(self):
        print(self.name)

if __name__ == "__main__":
    circ = Circle("circle", 6)
    circ.Area()
    circ.Perimeter()