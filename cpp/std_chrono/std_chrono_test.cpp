/* std_chrono_test.cpp
 *
 * Learning about the std::chrono library
 */

#include <chrono>
#include <iostream>


int main()
{
	using namespace std::chrono_literals; // used to get 1s numeric literal

	std::chrono::nanoseconds ns(1);
	std::chrono::nanoseconds sec(1s);

	std::cout << "One nanosecond = " << ns.count() << " nanoseconds" << std::endl;
	std::cout << "One second = " << sec.count() << " nanoseconds" << std::endl;
}
