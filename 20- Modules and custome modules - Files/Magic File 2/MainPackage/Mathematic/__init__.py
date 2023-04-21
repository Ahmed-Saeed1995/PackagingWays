print("Run automatically while loading module")

import os
import imp

path = os.getcwd() + "\MainPackage\Mathematic"

Rectangle = imp.load_source("",path + "\\rectangle.py" )


__all__ = ["FuncName", "VarName", "circle", "rectangle", "square", "trapezium", "triangle", "Rectangle"]



VarName = "This variable is from __init__.py file"


def FuncName(x, y, sign = "+"):
    return eval(f"{x} {sign} {y}")