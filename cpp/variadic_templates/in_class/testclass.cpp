
#include "testclass.h"
#include "log_interface.h"
#include "log_alternative.h"

template<typename DerivedLogger>
TestClass<DerivedLogger>::TestClass(LogInterface<DerivedLogger>& logger) : logger_(logger)
{

}

template<typename DerivedLogger>
void TestClass<DerivedLogger>::test_logging()
{
	logger_.log("Logging from test class cpp");
}


/** Necessary to avoid linker errors. 
 * See https://isocpp.org/wiki/faq/templates#separate-template-class-defn-from-decl
 */
template class TestClass<LogDefault>;
template class TestClass<LogAlternative>;
