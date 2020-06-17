
#include "testclass.h"
#include "vtemp_virtual.h"

/**
 * It works to define these functions in testclass.h, but not here
 */
template<typename DerivedLogger>
TestClass<DerivedLogger>::TestClass(LogInterface<DerivedLogger>& logger) : logger_(logger)
{

}

template<typename DerivedLogger>
void TestClass<DerivedLogger>::test_logging()
{
	logger_.log("Logging from test class");
}
