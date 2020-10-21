#include "testclass.h"
#include "abstract_obj.h"

int main()
{
	TestClass<DerivedObj> tc;

	tc.test_print();

}
