/* first.cpp
 * Simple first eigen program, from 
 * http://eigen.tuxfamily.org/dox/GettingStarted.html
 *
 * Assuming eigen is installed in /usr/local/include/eigen/
 * Compile with g++ -I /usr/local/include/eigen/ first.cpp
 * 28-MAR-2019
 */

#include <iostream>
#include <Eigen/Dense>

using Eigen::MatrixXd;

int main() 
{
	MatrixXd m(2,2);
	m(0, 0) = 3;
	m(1, 0) = 2.5;
	m(0, 1) = -1;
	m(1, 1) = m(1, 0) + m(0, 1);

	std::cout << m << std::endl;
}
