
LoadedModule = __import__("GeneralShape", globals = {'__name__':"MainPackage.Mathematic.GeneralShape"}
, level = 0 if __name__ == "__main__" else 1)

Shape = LoadedModule.Shape

class Rectangle(Shape):
    
    def __init__(self, name, legth, width):
        super().__init__(name)
        self.legth = legth
        self.width= width

    def Area(self):
        area = self.legth * self.width
        print(f"The area of a {self.name} is {area}")
        return area

    def Perimeter(self):
        perimeter = 2 * (self.legth + self.width)
        print(f"The perimeter of a {self.name} is {perimeter} ")
        return perimeter

    def ShapeName(self):
        print(self.name)

rec = Rectangle("retangle", 14, 8)
rec.Area()
rec.Perimeter()