#include <iostream>
#include <Eigen/Dense>

template <typename Scalar>
void processEigenMatrix(Eigen::Matrix<Scalar, 6, 1> &outputMatrix, const Eigen::Matrix<Scalar, 6, 1> inputMatrix)
{
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            outputMatrix[i] += inputMatrix[j];
        }
    }
    Eigen::Matrix<Scalar, 6, 6> temp = outputMatrix * inputMatrix.transpose();
    Scalar stemp = outputMatrix.transpose() * temp * inputMatrix;
    std::cout << "stemp = " << stemp << std::endl;
}

// Template function that accepts a 6x1 Eigen matrix with arbitrary scalar type
template <typename T>
void printEigenMatrix(const Eigen::Matrix<T, 6, 1> inputMatrix)
{
    for (int i = 0; i < 6; i++)
    {
        std::cout << "Element " << i << ": " << inputMatrix(i, 0) << std::endl;
    }
}

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
