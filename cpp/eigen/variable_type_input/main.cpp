#include <iostream>
#include <Eigen/Dense>
#include "eigenstuff.h"

int main()
{
    // Example usage with double scalar type
    Eigen::Matrix<double, 6, 1> matrixDouble;
    matrixDouble << 1.0, 2.0, 3.0, 4.0, 5.0, 6.0;

    Eigen::Matrix<double, 6, 1> matrixDoubleOut;
    matrixDoubleOut << 0, 0, 0, 0, 0, 0;
    processEigenMatrix(matrixDoubleOut, matrixDouble);
    printEigenMatrix(matrixDoubleOut);

    // Example usage with int scalar type
    Eigen::Matrix<int, 6, 1>
        matrixInt;
    matrixInt << 1, 2, 3, 4, 5, 6;

    Eigen::Matrix<int, 6, 1> matrixIntOut = Eigen::MatrixXi::Zero(6, 1);
    matrixIntOut << 0, 0, 0, 0, 0, 0;
    processEigenMatrix(matrixIntOut, matrixInt);
    printEigenMatrix(matrixIntOut);

    return 0;
}
