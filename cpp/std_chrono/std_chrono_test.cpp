/* std_chrono_test.cpp
 *
 * Learning about the std::chrono library
 */

#include <chrono>
#include <iostream>
using namespace std::chrono_literals; // used to get 1s numeric literal

void print_plus_ten_ns(std::chrono::milliseconds t)
{
	std::cout << t.count() << " + 10ns = " << (t + 10ns).count() << "ns" << std::endl;
}

int main()
{

	std::chrono::nanoseconds ns(1);
	std::chrono::nanoseconds sec(1s);

	std::cout << "One nanosecond = " << ns.count() << " nanoseconds" << std::endl;
	std::cout << "One second = " << sec.count() << " nanoseconds" << std::endl;

	std::cout << "One us + one ns = " << std::chrono::nanoseconds(1ns + 1us).count() << " nanoseconds" << std::endl;

	// When performing arithmetic, it uses the smallest base (nanoseconds here)
	std::cout << "One ns - one us = " << (1ns - 1us).count() << " nanoseconds" << std::endl;
	std::cout << "abs(One ns - one us) = " << std::chrono::abs(1ns - 1us).count() << " nanoseconds" << std::endl;

	std::cout << "1.95*(10ns) = " << std::chrono::duration_cast<std::chrono::nanoseconds>(1.95*10ns).count() << " nanoseconds" << std::endl;

	std::cout << "778e6 nanoseconds = " << std::chrono::duration<double>(778e6ns).count() << " seconds" << std::endl;

	print_plus_ten_ns(std::chrono::milliseconds(1));
}
