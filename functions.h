

const double pi = 3.141592653589793;
const double e = 216.0 / 24389.0;
const double k =  24389.0 / 27.0;

double radians(double deg);

double degress(double rad);

void rgb_to_srgb(double rgb[3]);

void srgb_to_linear(double srgb[3]);

void linear_to_xyz(double linear[3]);

double f_x(double x);

void xyz_to_lab(double xyz[3]);

double delta_e_cie2000_(double Lab1[3], double Lab2[3]);
