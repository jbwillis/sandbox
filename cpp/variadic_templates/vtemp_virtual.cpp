/** vtemp_printf.cpp
 * Experimenting with using variadic templates for
 * passing variable numbers of arguments to a function.
 *
 * Pass variable arguments to printf.
 *
 * Requires C++11.
 * 
 * Compile with: 
 * 		g++ -std=c++11 vtemp_adder.cpp
 */

#include<string>
#include<sstream>

#include<stdio.h>

template<typename Derived>
class LogInterface
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		Derived& derived = static_cast<Derived&>(*this);
		derived.log(fmt, args...);
	}
	
};

class LogDerived : public LogInterface<LogDerived>
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		std::stringstream ss;
		ss << "LOG: " << fmt;
		printf(ss.str().c_str(), args...);
	}
};

int main()
{
	LogInterface<LogDerived> logger;
	logger.log("Here's an int (%d)\t a str (%s)\t and a float (%e)\t\n",
			123, "boom", 3.1415);
}

