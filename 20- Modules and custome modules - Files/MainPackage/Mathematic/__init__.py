print("Run automatically while loading module")



__all__ = ["FuncName", "VarName", "circle", "rectangle", "square", "trapezium", "triangle"]



VarName = "This variable is from __init__.py file"


def FuncName(x, y, sign = "+"):
    return eval(f"{x} {sign} {y}")