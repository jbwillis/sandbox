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

#include "vtemp_virtual.h"
#include "testclass.h"

template<typename DerivedLogger>
void log_stuff(LogInterface<DerivedLogger>& logger)
{
	logger.log("Logging stuff %d", 4321); 
}

int main()
{
	LogInterface<LogDerived> logger;
	log_stuff(logger);

	TestClass<LogDerived>* tc = new TestClass<LogDerived>(logger);
	tc->test_logging();
}

