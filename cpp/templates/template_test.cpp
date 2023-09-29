#include <iostream>

template <typename T1, typename T2>
double myadder(T1 x, T2 y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    double a = 2.3;
    double b = 3.5;
    int c = 2;
    double ab = myadder(a, b);
    double cb = myadder(c, b);
    std::cout << "adder(a, b) = " << ab << std::endl;
    std::cout << "adder(c, b) = " << cb << std::endl;
}