from numba import njit
import numpy as np


from numba import njit
import numpy as np


class Color_Diff:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculus(self):
        color_a = self.rgb2srgb(self.a[0], self.a[1], self.a[2])
        color_b = self.rgb2srgb(self.b[0], self.b[1], self.b[2])

        xyz_a = self.srgb2xyz(color_a)
        xyz_b = self.srgb2xyz(color_b)

        lab_a = self.xyz2lab(xyz_a, function)
        lab_b = self.xyz2lab(xyz_b, function)

        delta = self.delta_e_cie_2000(lab_a, lab_b)
        
        return delta
    
    @staticmethod
    @njit(nopython=True)
    def rgb2srgb(r, g, b, srgb_=False):
        if srgb_:
            return np.array([r ** 2.2, g ** 2.2, b ** 2.2])
    
        else:
            return np.array([r / 255, g / 255, b / 255])
    @staticmethod
    @njit(nopython=True)
    def srgb2_new_srgb(srgb):
        srgb_new = np.array([0.0, 0.0, 0.0])
        for i in range(len(srgb)):
            if srgb[i] <= 0.04045:
                srgb_new[i] = srgb[i] / 12.92
    
            else:
                srgb_new[i] = ((srgb[i] + 0.055) / 1.055) ** 2.4
    
        return srgb_new
    
    @staticmethod       
    @njit(nopython=True)
    def srgb2xyz(srgb_new):
    
        r, g, b = srgb_new
        
        matrix_5 = np.array([0.4124 * r + 0.3576 * g + 0.1805 * b,
                             0.2126 * r + 0.7152 * g + 0.0722 * b,
                             0.0193 * r + 0.1192 * g + 0.9505 * b])
    
        rs, gs, bs = matrix_5
    
        rs = max(rs, 0.0)
        gs = max(gs, 0.0)
        bs = max(bs, 0.0)
    
        xyz = np.array([rs, gs, bs])
    
        return xyz
    
    @staticmethod
    @njit(nopython=True)
    def function(t):
        
        episilon = 0.008856
    
        kappa = 7.787
    
        if t > episilon:
            return t ** (1 / 3)
    
        else:
            return (t * kappa + 16) / 116
    
    @staticmethod
    @njit(nopython=True)
    def xyz2lab(xyz, f):
        Xn, Yn, Zn = (0.95047, 1.00000, 1.08883)
        X, Y, Z = xyz
        L = 116 * f(Y / Yn) - 16
        a = 500 * ((f(X / Xn) - f(Y / Yn)))
        b = 200 * ((f(Y / Yn) - f(Z / Zn)))
    
        return np.array([L, a, b])
    
    @staticmethod
    @njit(nopython=True)
    def delta_e_cie_2000(color_1, color_2):
        L1, a1, b1 = color_1
        L2, a2, b2 = color_2
    
        L_m = (L1 + L2) / 2
    
        C1 = (a1 ** 2 + b1 ** 2) ** (1 / 2)
        C2 = (a2 ** 2 + b2 ** 2) ** (1 / 2)
    
        C_m = (C1 + C2) / 2
    
        G = 1 / 2 * (1 - (C_m ** 7 / (C_m ** 7 + 25 ** 7)) ** (1 / 2))
    
        a1_ = a1 * (1 + G)
        a2_ = a2 * (1 + G)
    
        if a1_ == 0.0:
            a1_ = 0.00001
    
        if a2_ == 0.0:
            a2_ = 0.00001
    
        C1_ = (a1_ ** 2 + b1 ** 2) ** (1 / 2)
    
        C2_ = (a2_ ** 2 + b2 ** 2) ** (1 / 2)
    
        C_m_ = (C1_ + C2_) / 2
    
        h1_ = 0
    
        h2_ = 0
    
        if np.degrees(np.arctan(b1 / a1_)) >= 0:
            h1_ = np.degrees(np.arctan(b1 / a1_))
    
        else:
            h1_ = np.degrees(np.arctan(b1 / a1_)) + 360
    
        if np.degrees(np.arctan(b2 / a2_)) >= 0:
            h2_ = np.degrees(np.arctan(b2 / a2_))
    
        else:
            h2_ = np.degrees(np.arctan(b2 / a2_)) + 360
    
        H_m_ = 0
    
        if abs(h1_ - h2_) > 180:
            H_m_ = (h1_ + h2_ + 360) / 2
    
        else:
            H_m_ = (h1_ + h2_) / 2
    
        T = 1 - 0.17 * np.cos(np.radians(H_m_ - 30)) + 0.24 * np.cos(np.radians(2 * H_m_)) + 0.32 * np.cos(np.radians(3 * H_m_ + 6)) - 0.20 * np.cos(np.radians(4 * H_m_ - 63))
    
        delta_h_ = 0
    
        if abs(h2_ - h1_) <= 180:
            delta_h_ = h2_ - h1_
    
        elif abs(h2_ - h1_) > 180 and h2_ <= h1_:
            delta_h_ = h2_ - h1_ + 360
    
        else:
            delta_h_ = h2_ - h1_ - 360 
    
        delta_L_ = L2 - L1
    
        delta_C_ = C2_ - C1_
    
        delta_H_ = 2 * ((C1_ * C2_) ** (1 / 2)) * np.sin(np.radians(delta_h_) / 2)
    
        Sl = 1 + (0.015 * (L_m - 50) ** 2 / (20 + (L_m - 50) ** 2) ** (1 / 2))
    
        Sc = 1 + 0.045 * C_m_
    
        Sh = 1 + 0.015 * C_m_ * T
    
        delta_theta = 30 * np.exp((-((H_m_ - 275) / 25) ** 2))
    
        Rc = 2 * (C_m_ ** 7 / (C_m_ ** 7 + 25 ** 7)) ** (1 / 2)
    
        Rt = -Rc * np.sin(2 * np.radians(delta_theta))
    
        Kl = 1
    
        Kc = 1
    
        Kh = 1
    
        delta_e = ((delta_L_ / (Kl * Sl)) ** 2 + (delta_C_ / (Kc * Sc)) ** 2 + (delta_H_ / (Kh * Sh)) ** 2 + Rt * (delta_C_ / (Kc * Sc)) * (delta_H_ / (Kh * Sh))) ** (1 / 2)
    
        return delta_e

