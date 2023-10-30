#include <iostream>
#include <cmath>

int main(int argc, char **argv)
{
    double a = 0.0;
    double d = 1.0;
    double b = (1 - 5 * pow(a / d, 2)) * a / d;
    double c = b * 0.0001;

    printf("a = %e, b = %e, c = %e\n", a, b, c);
}