/** vtemp_adder.cpp
 * Experimenting with using variadic templates for
 * passing variable numbers of arguments to a function.
 *
 * Adder example from
 * https://eli.thegreenplace.net/2014/variadic-templates-in-c/
 *
 *
 * Requires C++11.
 * 
 * Compile with: 
 * 		g++ -std=c++11 vtemp_adder.cpp
 */

#include<iostream>
#include<string>


template <typename T>
T adder(T v) 
{
	std::cout << __PRETTY_FUNCTION__ << "\n";
	return v;
}

template<typename T, typename ... Args>
T adder(T first, Args... args)
{
	std::cout << __PRETTY_FUNCTION__ << "\n";
	return first + adder(args...);
}


int main()
{
	auto res1 = adder(1, 2, 3, 4, 5);
	std::cout << "adder(1, 2, 3, 4, 5) = " << res1 << "\n\n";

	std::string s1 = "he", s2 = "llo", s3 = ", ", s4 = "wor", s5 = "ld!";
	auto res2 = adder(s1, s2, s3, s4, s5);
	std::cout << "adder('he', 'llo', ', ', 'wor', 'ld!') = " << res2 << "\n\n";

}

