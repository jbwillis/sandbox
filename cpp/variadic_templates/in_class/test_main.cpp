/** vtemp_printf.cpp
 * Experimenting with using variadic templates for
 * passing variable numbers of arguments to a function.
 *
 * Pass variable arguments to printf.
 *
 * Requires C++11.
 * 
 * Compile with: 
 * 		g++ -std=c++11 test_main.cpp testclass.cpp
 *
 */

#include "log_interface.h"
#include "log_alternative.h"
#include "testclass.h"

template<typename DerivedLogger>
void log_stuff(LogInterface<DerivedLogger>& logger)
{
	logger.log("Logging stuff %d", 4321); 
}

int main()
{
	// Default Logger
	LogDefault logger_d;
	log_stuff(logger_d);

	TestClass<LogDefault> tc_d(logger_d);
	tc_d.test_logging();

	// Alternative Logger
	LogAlternative logger_a;
	log_stuff(logger_a);

	TestClass<LogAlternative> tc_a(logger_a);
	tc_a.test_logging();
}

