from abc import abstractmethod, ABCMeta, ABC

class Shape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Area(self):
        Ellipsis

    @abstractmethod
    def Perimeter(self):
        ...

    @abstractmethod
    def ShapeName(self):
        pass