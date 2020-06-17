
#ifndef _VTEMP_VIRTUAL_H_
#define _VTEMP_VIRTUAL_H_


#include<string>
#include<sstream>
#include<stdio.h>

class LogInterfaceVirtual
{
public:
	template <typename... T>
	virtual void log(const char* fmt, const T&... args) = 0;
};

template<typename Derived>
class LogInterface : LogInterfaceVirtual
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		Derived& derived = static_cast<Derived&>(*this);
		derived.log(fmt, args...);
	}
	
};

class LogDerived : public LogInterface<LogDerived>
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		std::stringstream ss;
		ss << "LOG: " << fmt << "\n";
		printf(ss.str().c_str(), args...);
	}
};

#endif /* _VTEMP_VIRTUAL_H_ */
