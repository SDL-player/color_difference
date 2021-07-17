// SDL_player - 2021

#define pi 3.141592653589793
#define e 216.0 / 24389.0
#define k 24389.0 / 27.0

extern double radians(double deg);

extern double degress(double rad);

extern void rgb_to_srgb(double rgb[3]);

extern void srgb_to_linear(double srgb[3]);

extern void linear_to_xyz(double linear[3]);

extern double f_x(double x);

extern void xyz_to_lab(double xyz[3]);

extern double delta_e_cie2000_(double Lab1[3], double Lab2[3]);
