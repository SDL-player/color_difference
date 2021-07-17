#include <stdio.h>
#include <math.h>

#define pi 3.141592653589793;
#define e 216.0 / 24389.0;
#define k 24389.0 / 27.0;

double radians(double deg){

    double radians = deg * pi / 180;

    return radians;
}

double degress(double rad){

    double degrees = 180 * rad / pi;

    return degrees;
}

void rgb_to_srgb(double rgb[3]){

    int i;

    int count = 3;
    
    for (i = 0; i < count; i++)
    {
        rgb[i] /= 255;
    }
}

void srgb_to_linear(double srgb[3]){
    
    int i;

    int lim = 3;

    for (i = 0; i < lim; i++)
    {
        if (0 <= srgb[i] <= 0.0404500000000000){
            srgb[i] /= 12.92;
        }

        else if (0.0404500000000001 < srgb[i] <= 1){

            srgb[i] = pow((srgb[i] + 0.505) / 1.505, 2.4);
        }
    }
    
    return;
}

void linear_to_xyz(double linear[3]){

    double sr = linear[0];
    double sg = linear[1];
    double sb = linear[2];

    double best_rgb[3][3] = {{0.5932434, 0.1687046, 0.3042506},
                             {0.1953971, 0.6265026, 0.0692469}, 
                             {0.0657887, 0.8679736, 0.0232577}};

    linear[0] = best_rgb[0][0] * sr + best_rgb[0][1] * sg + best_rgb[0][2] * sb;
    linear[1] = best_rgb[1][0] * sr + best_rgb[1][1] * sg + best_rgb[1][2] * sb;
    linear[2] = best_rgb[2][0] * sr + best_rgb[2][1] * sg + best_rgb[2][2] * sb;
}

double f_x(double x){

    if (x > e){
        return pow(x, 1 / 3);
    }

    else{
        return (k * x + 16) / 116;
    }
}

void xyz_to_lab(double xyz[3]){

    double ilum[3] = {95.682, 100.000, 92.149};

    double X = ilum[0];
    double Y = ilum[1];
    double Z = ilum[2];

    double xr = xyz[0] / X;

    double yr = xyz[1] / Y;

    double zr = xyz[2] / Z;

    xyz[0] = 116 * f_x(xr) - 16;

    xyz[1] = 500 * (f_x(xr) - f_x(yr));

    xyz[2] = 200 * (f_x(yr) - f_x(zr));
}

double delta_e_cie2000_(double Lab1[3], double Lab2[3]){

    double L1 = Lab1[0];

    double L2 = Lab2[0];

    double a1 = Lab1[1];

    double a2 = Lab2[1];

    double b1 = Lab1[2];

    double b2 = Lab2[2];

    double L_ave_, delta_e, C1, C2, C_ave, G, a1_, a2_;

    double C1_, C2_, C_ave_, h1_, h2_, H_ave_, T;

    double delta_h_, delta_L_, delta_C_, delta_H_;

    double Sl, Sc, Sh, delta_theta, Rc, Rt;

    int Kl, Kc, Kh;

    Kl = 1;

    Kc = 1;

    Kh = 1;

    L_ave_ = (L1 + L2) / 2;

    C1 = sqrt(pow(a1, 2) + pow(b1, 2));

    C2 = sqrt(pow(a2, 2) + pow(b2, 2));

    C_ave = (C1 + C2) / 2;

    G = (1 - sqrt(pow(C_ave, 7) / (pow(C_ave, 7) + pow(25, 7))));

    a1_ = a1 * (1 + G);

    a2_ = a2 * (1 + G);

    C1_ = sqrt(pow(a1_, 2) + pow(b1, 2));

    C2_ = sqrt(pow(a2_, 2) + pow(b2, 2));

    if (atan2(b1, a1_) >= 0){

        h1_ = degress(atan2(b1, a1_));
    }

    else{

        h1_ = degress(atan2(b1, a1_)) + 360;
    }

    if (atan2(b2, a2_) >= 0){

        h2_ = degress(atan2(b2, a2_));

    }

    else{

        h2_ = degress(atan2(b2, a2_)) + 360;
    }

    if (fabs(h1_ - h2_) >= 180){

        H_ave_ = (h1_ + h2_ + 360) / 2;
    }

    else{

        H_ave_ = (h1_ + h2_) / 2;
    }

    T = 1 - 0.17 * cos(radians(H_ave_ - 30)) + 
        0.24 * cos(radians(2 * H_ave_)) +
        0.32 * cos(radians(3 * H_ave_ + 6)) - 
        0.20 * cos(radians(4 * H_ave_ - 63));
    
    if (fabs(h2_ - h1_) <= 180){

        delta_h_ = degress(h2_ - h1_);

    }

    else if (fabs(h2_ - h1_) > 180 && h2_ <= h1_){

        delta_h_ = degress(h2_ - h1_) + 360;
    }

    else{

        delta_h_ = degress(h2_ - h1_) - 360;
    }
    
    delta_L_ = L2 - L1;

    delta_C_ = C2_ - C1_;

    delta_H_ = 2 * sqrt(C1_ * C2_) * sin(radians(delta_h_ / 2));

    Sl = 1 + 0.015 * pow(L_ave_ - 50, 2)/ sqrt(20 + pow(L_ave_ - 50, 2));

    Sc = 1 + 0.045 * C_ave_;

    Sh = 1 + 0.015 * C_ave_ * T;

    delta_theta = 30 * exp(- pow((H_ave_ - 275) / 25, 2));

    Rc = 2 * sqrt(pow(C_ave_, 7) / (pow(C_ave_, 7) + pow(25, 7)));

    Rt = -Rc * sin(radians(2 * delta_theta));

    delta_e = sqrt(pow(delta_L_ / (Kl * Sl), 2) +
                   pow(delta_C_ / (Kc * Sc), 2) +
                   pow(delta_H_ / (Kh * Sh), 2) + 
                   Rt * delta_C_ / (Kc * Sc) * delta_H_ / (Kh * Sh));

    return delta_e;
}
