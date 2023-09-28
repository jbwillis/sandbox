#pragma once
#include <Eigen/Dense>
#include <iostream>

/*
Two options for ensuring template functions are found by the linker:
 - include the definition in the .h file so the definition is available when it is clear
   what instantiation is needed in the code.
 - include each expected instantiation at the end of the .cpp file (see eigenstuff.cpp for an example).
   Then the compiler instantiates the function for each template when it compiles the .cpp file.
   In a large project this can potentially reduce the program size as it reduces the number of duplicate
   template functions that are generated.

See: https://isocpp.org/wiki/faq/templates#separate-template-fn-defn-from-decl
*/

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
void printEigenMatrix(const Eigen::Matrix<T, 6, 1> inputMatrix);
