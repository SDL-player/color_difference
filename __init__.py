from ctypes import *

functions = CDLL("functions.dll")

rgb2srgb = functions.rgb_to_srgb

srgb2linear = functions.srgb_to_linear

linear2xyz = functions.linear_to_xyz

xyz2Lab = functions.xyz_to_lab

delta_cie_2000_ = functions.delta_e_cie2000_

delta_cie_2000_.restype = c_double
        
def color_diff(a, b):
    
    """Calculate the delta_e_cie_2000 between two values in rgb format."""
        
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
