#include <string>
#include <stdio.h>


void print_two_nums_2(const char* format, int num1, int num2)
{
	printf(format, num1, num2);
}

void print_two_nums(const char* format, int num1, int num2)
{
	print_two_nums_2(format, num1, num2);
}

template<typename ... T>
void print_variadic(const char* format, const T&... args)
{
	printf(format, args...);
}

template<typename ... T>
void print_variadic_2(const char* format, const T&... args)
{
	print_variadic(format, args...);
}

int main()
{
	print_two_nums("Print %d, %d\n", 1, 2);

	std::string f ("%s, %d\n");
	print_variadic_2(f.c_str(), "Hello", 77);
}
