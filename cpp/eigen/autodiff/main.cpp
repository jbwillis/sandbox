#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/AutoDiff>

template <typename T>
T quadratic_form(const Eigen::Matrix<double, 3, 3> Q, const Eigen::Matrix<T, 3, 1> x)
{
    return 0.5 * x.dot(Q * x);
}

template <typename T>
void quadratic_form_dx(Eigen::Matrix<T, 1, 3> &r, const Eigen::Matrix<double, 3, 3> Q, const Eigen::Matrix<T, 3, 1> x)
{
    r = x.transpose() * Q;
}

template <typename T>
void quadratic_form_ddx(Eigen::Matrix<double, 3, 3> &R, Eigen::Matrix<double, 3, 3> Q, const Eigen::Matrix<T, 3, 1> x)
{
    R = Q;
}

int main(int argc, char **argv)
{
    std::cout << "Testing Eigen's Autodiff Functionality" << std::endl;
    Eigen::Matrix<double, 3, 3> Q;
    Q << 1.0, 0.0, 0.0,
        0.0, 2.0, 0.0,
        0.0, 0.0, 3.0;

    Eigen::Matrix<double, 3, 1> x;
    x << 1.0, 1.0, 1.0;

    std::cout << "x'Qx/2 = " << quadratic_form(Q, x) << std::endl;
    Eigen::Matrix<double, 1, 3> r;
    quadratic_form_dx(r, Q, x);
    std::cout << "dx = " << r << std::endl;
    Eigen::Matrix<double, 3, 3> R;
    quadratic_form_ddx(R, Q, x);
    std::cout << "ddx = \n"
              << R << std::endl;
}