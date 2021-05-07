#include "testclass.h"
#include "abstract_obj.h"


template<typename Impl>
TestClass<Impl>::TestClass()
{
	obj_ = &AbstractObj<Impl>("Samwise Gamgee");
}

template<typename Impl>
void TestClass<Impl>::test_print()
{
	obj_.printName();
}


template class TestClass<DerivedObj>;
