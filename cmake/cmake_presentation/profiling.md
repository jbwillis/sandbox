Code Profiling
==============

From [Wikipedia](https://en.wikipedia.org/wiki/Profiling_(computer_programming):
"In software engineering, profiling is a form of **dynamic program analysis** that measures, for example, the space (memory) or time complexity of a program, the usage of particular instructions, or the frequency and duration of function calls. Most commonly, **profiling information serves to aid program optimization**."


There are three major methods for performing profiling:

  * **Event-based**: For interpreted languages such as python or for languages run by a virtual machine (java), it is possible to use the superstructure running the program to monitor the running program.
  * **Statistical**: These profilers sample the running program, creating a statistical approximation of its runtime performance.
    * Pros: Not very intrusive
    * Cons: Statistical, so may not capture true program behavior
  * **Instrumentation**: This involves adding (automatically or manually) code to the program that measures and reports characteristics of the program as it runs.
    * Pros: Highly granular, can catch many types of problems
    * Cons: Can significantly increase program runtime (Valgrind runs programs to run 20-30 times slower), may introduce new bugs (Heisenbugs!)

## Commonly Used Open Source Profiling Tools
* [gprof](https://sourceware.org/binutils/docs/gprof/)
	* Uses a combination of statistical and instrumentation based approach. 
	* When compiling with `gcc` the `-pg` flag is used to add in gprof. 
	* Seems to be the standard GNU profiling tools. 
	* Major limitation: Does not support multi-threaded applications, shared libraries and kernel profiling.
* [oprofile](https://oprofile.sourceforge.io/about/)
	* System-wide profiler, requiring no special recompilation
	* Supports debugging of all code, including kernel, multi-threaded, and shared libraries
	* Requires root permissions
* [valgrind](http://www.valgrind.org/)
	* Instruments the program at runtime, using a sort of virtual machine to simulate the program.
	* Can produce a call graph using `callgrind`
	* Also can help find memory leaks and other bugs
* [gperftools](https://github.com/gperftools/gperftools)
	* Primarily a fast implementation of `malloc`, but it also includes a CPU profiler, heap profiler, and memory leak detector.
	* Supports statitistical (fast) profiling of multi-threaded programs.

## Resources
* [Comparison of **gperftools,** **Valgrind,** and **gprof**](http://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/)
* [Introduction to OProfile](http://wiki.ros.org/roslaunch/Tutorials/Profiling%20roslaunch%20nodes)
* [Profiling ROS nodes](http://wiki.ros.org/roslaunch/Tutorials/Profiling%20roslaunch%20nodes)
