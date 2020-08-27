#include <chrono>
#include <iostream>

void print_ns(std::chrono::nanoseconds t)
{
	std::cout << t.count() << "ns\n";
}

void print_s(std::chrono::seconds t)
{
	std::cout << t.count() << "s\n";
}

int main()
{
	// Converting from a lower precision to a higher precision 
	// without casting works (compiles properly)
	print_ns(std::chrono::microseconds(10));
	print_ns(std::chrono::milliseconds(10));

	// These lines won't compile, to convert from a higher precision 
	// to a lower precision, a duration_cast is necessary.
	//
	//print_s(std::chrono::microseconds(10));
	//print_s(std::chrono::milliseconds(10));
	
	print_s(std::chrono::duration_cast<std::chrono::seconds> (std::chrono::microseconds(10)));
	print_s(std::chrono::duration_cast<std::chrono::seconds> (std::chrono::milliseconds(10)));

}
