/* std_function_intro.cpp
 * 
 * Scratch space for learning how to use std::function,
 * particularly focusing on defining a consistent type
 * for a callback function.
 */
#include <iostream>
#include <functional>

using void_function_type = std::function<void()>;

void hello_world()
{
	std::cout << "Hello, World!" << std::endl;
}

void greeting_world(std::string greeting_string)
{
	std::cout << greeting_string << ", World!" << std::endl;
}

void call_void_function(void_function_type f)
{
	f();
}


class HawaiianGreeting 
{
public:
	void greet() {
		std::cout << "Aloha!" << std::endl;
	}
};

int main()
{

	void_function_type f1 = std::bind(&hello_world);
	void_function_type f2 = std::bind(&greeting_world, "Howdy");
	void_function_type f3 = std::bind(&greeting_world, "Hola");

	HawaiianGreeting hg;
	void_function_type f4 = std::bind(&HawaiianGreeting::greet, &hg);

	f1();
	call_void_function(f2);
	call_void_function(f3);
	call_void_function(f4);
}
