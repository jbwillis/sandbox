#include "eigenstuff.h"

// Template function that accepts a 6x1 Eigen matrix with arbitrary scalar type
template <typename T>
void printEigenMatrix(const Eigen::Matrix<T, 6, 1> inputMatrix)
{
    for (int i = 0; i < 6; i++)
    {
        std::cout << "Element " << i << ": " << inputMatrix(i, 0) << std::endl;
    }
}

template void printEigenMatrix<int>(const Eigen::Matrix<int, 6, 1>);
template void printEigenMatrix<double>(const Eigen::Matrix<double, 6, 1>);