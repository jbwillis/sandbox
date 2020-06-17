
#ifndef _TEST_CLASS_H_
#define _TEST_CLASS_H_

#include "vtemp_virtual.h"


template<typename DerivedLogger>
class TestClass
{
public:
	TestClass(LogInterface<DerivedLogger>& logger) : logger_(logger)
{

}
	void test_logging()
{
	logger_.log("Logging from test class");
}

private:
	LogInterface<DerivedLogger>& logger_;
};

#endif /* _TEST_CLASS_H_ */
