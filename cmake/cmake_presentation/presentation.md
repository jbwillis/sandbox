# CMake and Code Profiling

![](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

---

# Definitions

These may not be perfect definitions, but they are good enough for now.

* Executable - the result of compiling a c/c++ program. 
* Library - a pre-compiled piece of software that your program relies on.
	* Static - compiled library code is included in code for final program
	* Shared - compiled library code is linked in during the execution of the program

---

# Make vs CMake - A Simple Example
We will use the following three files for a simple hello world program [ref](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/). 

**main.c**

	!cpp
	#include "helloworld.h"
	int main() {
		helloWorld();
		return 0;
	}


**helloworld.c**

	!cpp
	#include <stdio.h>
	#include "helloworld.h"
	void helloWorld() {
		printf("Hello World!\n");
	}

**helloworld.h**

	!cpp
	#ifndef HELLO_WORLD_H_
	#define HELLO_WORLD_H_
	void helloWorld();
	#endif /* HELLO_WORLD_H_ */

---
# Simple Example - File Org
These files are arranged in the following directory structure, where * is either Make or CMake. 

	simple_example_*/
	├── build
	├── include
	│   └── helloworld.h
	└── src
		├── helloworld.c
		└── main.c

---
# Compiling on command line
When compiling this program, you might run:

	!bash
	gcc -o build/main src/main.c src/helloworld.c -Iinclude/

* Quick for small programs
* No documented/repeatable method for compiling
* Recompiles all of the files, regardless of changes

This works fine for a program consisting of a couple of files, but quickly becomes unweildy. It requires you to recall the exact command you are using when compiling, and it recompiles all of the files, regardless of if they have been changed. Recompiling unchanged files becomes a significant waste of time on any but the the simplest projects.

---
# Makefiles

* Native UNIX system for building programs
* Compares the timestamps of the source files with those of the compiled object files, recompiling if the source file timestamp is more recent


Here's about the simplest makefile that could be used to compile our example:

	!makefile
	hellomake: main.c lib/helloworld/helloworld.c
		gcc -o build/main src/main.c \
		lib/helloworld/helloworld.c -Ilib/helloworld/

* Easy to recompile
* Not very easy to extend
* Still recompiles everything every time


---
# Makefiles
	!makefile
	CC=gcc
	IDIR=include
	CFLAGS=-I$(IDIR)
	SDIR=src
	BDIR=build

	_DEPS=helloworld.h
	_OBJ = helloworld.o main.o
	DEPS=$(patsubst %,$(IDIR)/%,$(_DEPS))
	OBJ = $(patsubst %,$(BDIR)/%,$(_OBJ))

	$(BDIR)/%.o: $(SDIR)/%.c $(DEPS)
		$(CC) -c -o $@ $< $(CFLAGS)

	main: $(OBJ)
		$(CC) -o $(BDIR)/$@ $^ $(CFLAGS) 

	.PHONY: clean
	clean:
		rm -f $(ODIR)/*.o *~ core $(IDIR)/*~ 

* Add additional files by modifying the `_DEPS` and `_OBJ` lines
* The `%.o` rule compiles each `.c` file into its own object files, which are then linked together at the end in the `main` rule. 

---

# Pros and Cons of Make
* Pros 			
	* Comes with any unix-like operating system 
	* Recompiles only changed files 
	* Can handle complicated build configurations 
* Cons			
	* Not compatible with non-unix systems
	* Timestamp based method is susceptible to errors, requiring a `make clean` to fix them.
	* Somewhat archaic language takes time to get used to 

---

# CMake
From the website: 

"CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner. Unlike many cross-platform systems, CMake is designed to be used in conjunction with the native build environment."

Put simply, **CMake is a program that generates makefiles (lots of them).**

---
# File Organization
Continuing our simple example, for CMake, we need to create two `CMakeLists.txt` files. One goes in the root of the project and the other in the src directory.

	simple_example_CMake/
	├── build
	├── CMakeLists.txt
	├── include
	│   └── helloworld.h
	└── src
		├── CMakeLists.txt
		├── helloworld.c
		└── main.c

---
# CMakeLists

**CMakeLists.txt**

	!cmake
	cmake_minimum_required (VERSION 2.8.3)
	project (Simple_Example)

	include_directories("${PROJECT_SOURCE_DIR}/include")
	add_subdirectory(src)

**src/CMakeLists.txt**

	!cmake
	add_library(helloworld STATIC helloworld.c)
	add_executable(main main.c)
	target_link_libraries(main helloworld)

---

CMake generates a lot of files, so it is common to create a `build` directory, and to run `cmake` from within that directory. In addition, since it is really just generating native build files, you must run `make` after running `cmake.` To compile the simple example:

	!bash
	$ cd build/
	$ cmake ..
	$ make

Then to run `main`:

	!bash
	$ build/src/main

---
# Building in ROS - Catkin
.notes: This assumes you are already familar with the basic structure of a catkin workspace, and how to build a set of ros packages.

## Catkin
<!--![](https://en.wikipedia.org/wiki/Catkin#/media/File:Willow_catkin_2_aka.jpg "Catkins on a willow")-->
![](catkin_300.jpg "https://en.wikipedia.org/wiki/Catkin#/media/File:Willow_catkin_2_aka.jpg")

* Essentially a wrapper for CMake that does some ros-specifiic things before calling cmake.

* When you run `catkin_make` in an empty catkin workspace (`~/catkin_ws`), [here is what is actually happening](http://wiki.ros.org/catkin/commands/catkin_make)

	!bash
	$ cd ~/catkin_ws
	$ cd src
	$ catkin_init_workspace
	$ cd ..
	$ mkdir build
	$ cd build
	$ cmake ../src -DCMAKE_INSTALL_PREFIX=../install -DCATKIN_DEVEL_PREFIX=../devel
	$ make

.notes: The `catkin_init_workspace` command creates the top level CMakelists.txt as a symlink to a generic one found in the ros installation. Note that at the end, `cmake` is invoked on the `src` directory, and then `make` is called from within `build`.

---
# CMake - more depth
There are countless resources on CMake online. To give a good general overview of using CMake with ROS, we will use the `CMakeLists.txt` file from [roscopter](http://github.com/byu-magicc/roscopter/). 

---

# Improving the build - CCache
* make (and thus cmake) uses file timestamps to determine when it needs to recompile a file. 
* ccmake hashes the source file and compiler arguments and stores the compiled object files in a cache. 
* Installing ccmake reduced the time it took for a clean recompile of roscoptor from ~50 sec to ~20 sec, including the time cmake spends regenerating files. 

.notes: There are times when files have not changed, but the timestamp has (such as on a git checkout). Additionally, on a `make clean; make` many of the built files will not change, but on a large project you will wait a long time for them to rebuild. Finally, if you are working on multiple copies of the same project (such as rosflight in roscopter and rosplane), you might be recompiling much of the same code. 

--- 
# Installing CCache

* Use the [instructions!](https://github.com/ccache/ccache/blob/master/doc/INSTALL-from-release-archive.md)
* I used their most recent archive (3.7.1) 
* ccache forms an "invisible" layer on top of the regular compiler. Create symbolic links to ccache as they describe in their instructions. Catkin automatically sets CMake to use `/usr/bin/c++` so, you need to link that one too.

	!bash
	/usr/local/bin/c++ -> /usr/local/bin/ccache
	/usr/local/bin/cc -> /usr/local/bin/ccache
	/usr/local/bin/g++ -> /usr/local/bin/ccache
	/usr/local/bin/gcc -> /usr/local/bin/ccache

---
# Improving the build - Ninja
[Ninja](https://ninja-build.org/) is intended to speed up incremental builds. CMake (and thus Catkin) has built in support for generating ninja buildfiles. To run `catkin_make` with ninja, just pass the `--use-ninja` flag.

---

# References
* [ROS official justification for Catkin](http://wiki.ros.org/catkin/conceptual_overview)
* [catkin\_make command description page](http://wiki.ros.org/catkin/commands/catkin_make)
* [Catkin CMakeLists.txt explanation](http://wiki.ros.org/catkin/CMakeLists.txt)
* [Catkin workspaces explanation](http://wiki.ros.org/catkin/workspaces)
* [Makefile tutorial by Bruce Maxwell](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/) 
* [CMake Cookbook (Free from BYU Library)](https://learning.oreilly.com/library/view/cmake-cookbook/9781788470711/?ar)
	* [Example Code git repo](https://github.com/PacktPublishing/CMake-Cookbook)
* [ccache website](https://ccache.dev/)

---
# Code Profiling

"In software engineering, profiling is a form of **dynamic program analysis** that measures, for example, the space (memory) or time complexity of a program, the usage of particular instructions, or the frequency and duration of function calls. Most commonly, **profiling information serves to aid program optimization**."

From [Wikipedia](https://en.wikipedia.org/wiki/Profiling_(computer_programming))

---
# When should I profile?

![](https://imgs.xkcd.com/comics/optimization.png)

---

# Profiling Methods
  * **Event-based**: For interpreted languages such as python or for languages run by a virtual machine (java), it is possible to use the superstructure running the program to monitor the running program.
  * **Statistical**: These profilers sample the running program, creating a statistical approximation of its runtime performance.
    * Pros: Not very intrusive
    * Cons: Statistical, so may not capture true program behavior
  * **Instrumentation**: This involves adding (automatically or manually) code to the program that measures and reports characteristics of the program as it runs.
    * Pros: Highly granular, can catch many types of problems
    * Cons: Can significantly increase program runtime (Valgrind runs programs to run 20-30 times slower), may introduce new bugs (Heisenbugs!)

---

# Common Profiling Tools
## [gprof](https://sourceware.org/binutils/docs/gprof/)
* Uses a combination of statistical and instrumentation based approach. 
* When compiling with `gcc` the `-pg` flag is used to add in gprof. 
* Seems to be the standard GNU profiling tools. 
* Major limitation: Does not support multi-threaded applications, shared libraries and kernel profiling.
## [oprofile](https://oprofile.sourceforge.io/about/)
* System-wide profiler, requiring no special recompilation
* Supports debugging of all code, including kernel, multi-threaded, and shared libraries
* Requires root permissions

---

# Common Profiling Tools
## [valgrind](http://www.valgrind.org/)
* Instruments the program at runtime, using a sort of virtual machine to simulate the program.
* Can produce a call graph using `callgrind`
* Also can help find memory leaks and other bugs
## [gperftools](https://github.com/gperftools/gperftools)
* Primarily a fast implementation of `malloc`, but it also includes a CPU profiler, heap profiler, and memory leak detector.
* Supports statitistical (fast) profiling of multi-threaded programs.

---
# Resources
* [Comparison of **gperftools,** **Valgrind,** and **gprof**](http://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/)
* [Introduction to OProfile](http://wiki.ros.org/roslaunch/Tutorials/Profiling%20roslaunch%20nodes)
* [Profiling ROS nodes](http://wiki.ros.org/roslaunch/Tutorials/Profiling%20roslaunch%20nodes)
