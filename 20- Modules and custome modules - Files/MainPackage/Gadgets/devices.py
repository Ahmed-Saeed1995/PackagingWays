import csv
import os

path = os.getcwd() + "\MainPackage\Gadgets"

class Devices:
    AllDevices = []
    def __init__(self, Product, Rate, Price):
        self.Product = Product
        self.Rate = Rate
        self.Price = Price
        
        Devices.AllDevices.append(self)
        
    @classmethod
    def ClassMethod(cls):
        print("Run in the background")
        with open(path + "\devices.csv", "r") as f:
            gadgets = list( csv.DictReader(f))
            for gadget in gadgets:
                Devices( Product = gadget.get("Product"),
                       Rate = int(gadget.get("Rate")),
                       Price = float(gadget.get("Price")))
                
    def __repr__(self):
        return f"Devices('{self.Product}', '{self.Rate}', '{self.Price}')"