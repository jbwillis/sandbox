#ifndef _LOG_INTERFACE_H_
#define _LOG_INTERFACE_H_


#include<string>
#include<sstream>
#include<stdio.h>

template<typename Derived>
class LogInterface
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		Derived& derived = static_cast<Derived&>(*this);
		derived.log(fmt, args...);
	}
	
};

class LogDefault : public LogInterface<LogDefault>
{
public:
	template <typename... T>
	void log(const char* fmt, const T&... args)
	{
		std::stringstream ss;
		ss << "Default LOG: " << fmt << "\n";
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wformat-security"
		printf(ss.str().c_str(), args...);
#pragma GCC diagnostic pop
	}
};

#endif /* _LOG_INTERFACE_H_ */
