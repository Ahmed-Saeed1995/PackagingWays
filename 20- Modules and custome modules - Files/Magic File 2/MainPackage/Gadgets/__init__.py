print("Run automatically")

import os
import imp
import math
import string

path = os.getcwd() + "\MainPackage\Gadgets"
devices = imp.load_source("", path + "\devices.py")

Devices = devices.Devices
__all__ = ["math", "string"]


def FuncName():
    Devices.ClassMethod
    return Devices.AllDevices

