#ifndef _TEST_CLASS_H_
#define _TEST_CLASS_H_

#include "abstract_obj.h"


template<typename Impl>
class TestClass
{
public:
	TestClass() ;
	void test_print();

private:
	AbstractObj<Impl>& obj_;
};

#endif /* _TEST_CLASS_H_ */
