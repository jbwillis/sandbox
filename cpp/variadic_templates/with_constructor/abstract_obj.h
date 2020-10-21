#ifndef ABSTRACT_OBJ_H
#define ABSTRACT_OBJ_H

#include <iostream>
#include <string>

template <typename Derived>
class AbstractObj
{
public:
	virtual void AbstractObj(std::string name) = 0;

	void printName()
	{
		Derived& derived = static_cast<Derived&>(*this);
		derived.printName();
	}
};

class DerivedObj
{
public:
	DerivedObj(std::string name)
	{
		name_ = name;
	}

	void printName()
	{

		std::cout << "My name is " << name_ << std::endl;
	}

private:
	std::string name_;
};

#endif /* ABSTRACT_OBJ_H */
