from ctypes import *
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import time

functions = CDLL("functions.dll")

rgb2srgb = functions.rgb_to_srgb

srgb2linear = functions.srgb_to_linear

linear2xyz = functions.linear_to_xyz

xyz2Lab = functions.xyz_to_lab

delta_cie_2000_ = functions.delta_e_cie2000_

delta_cie_2000_.restype = c_double


class Color_Diff:
    
    def __init__(self, a, b):
        
        """Calculate the delta_cie_2000 between two values in rgb format."""
        
        self.a = a
        self.b = b
        
    def calculate(self):
        
        arr_ = (c_double * len(self.a))(*self.a)
        
        rgb2srgb(arr_)
        
        srgb2linear(arr_)
        
        linear2xyz(arr_)
        
        xyz2Lab(arr_)
        
        arr_2 = (c_double * len(self.b))(*self.b)
        
        rgb2srgb(arr_2)
        
        srgb2linear(arr_2)
        
        linear2xyz(arr_2)
        
        xyz2Lab(arr_2)
        
        delta = delta_cie_2000_(arr_, arr_2)
        
        return delta
    

color_1 = 255, 23, 209   

color_2 = 125, 28, 109

def color_diff(a, b):
    color_a = sRGBColor(a[0], a[1], a[2])
    
    color_b = sRGBColor(b[0], b[1], b[2])
    
    color_a_lab = convert_color(color_a, LabColor)
    
    color_b_lab = convert_color(color_b, LabColor)
    
    return delta_e_cie2000(color_a_lab, color_b_lab)
    
print(round(Color_Diff(color_1, color_2).calculate()), round(color_diff(color_1, color_2)))

lim = 100000

py = time.time_ns()

for i in range(lim): color_diff(color_1, color_2)

py = time.time_ns() - py

print(py / (10 ** 9))

c = time.time_ns()

for j in range(lim): Color_Diff(color_1, color_2)

c = time.time_ns() - c

print(c / (10 ** 9))

print(round(py / c))
