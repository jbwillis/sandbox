
#ifndef _TEST_CLASS_H_
#define _TEST_CLASS_H_

#include "log_interface.h"


template<typename DerivedLogger>
class TestClass
{
public:
	TestClass(LogInterface<DerivedLogger>& logger) ;
	void test_logging();

private:
	LogInterface<DerivedLogger>& logger_;
};

#endif /* _TEST_CLASS_H_ */
