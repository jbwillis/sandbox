# Using GDB to debug a program on an STM32F4
I am using a STM32F405 on an openpilot revolution flight controller board, 
but this should be applicable, perhaps with some modifications, on any STM32F4 board.

## Resources
* <http://docs.rosflight.org/en/latest/developer-guide/debugging/>
	* ROSflight instructions on using a debugger. These helped me get the right tools, 
	but are written assuming you will be debugging in Eclipse. I wanted to use GDB from
	the command line, so the last half of the instructions are less helpful.
* <openocd.org>
	* Openocd is a open source debugger project that will create a gdbserver for
	interacting with the STM32 hardware.
	* <http://openocd.org/doc/html/GDB-and-OpenOCD.html#GDB-and-OpenOCD>
		* This is a particularly useful page in the openocd documentation. It describes
		the process of connecting to the gdbserver started by openocd, and loading a 
		program to be run using GDB


## Hardware
* Openpilot revolution, with wires soldered on the JTAG connector
* ST-Link V2


## Software Set Up
* Install openocd
	* `$ sudo apt install openocd`
* Install ARM compiler (code from [ROSFlight Building and Flashing guide](http://docs.rosflight.org/en/latest/developer-guide/building-flashing/)
	* This installation includes gdb compiled for ARM devices
```
sudo apt install -y lib32ncurses5
wget https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2
tar -xvf gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2
sudo mv gcc-arm-none-eabi-5_4-2016q3 /opt/.
echo "export PATH=\$PATH:/opt/gcc-arm-none-eabi-5_4-2016q3/bin" >> ~/.bashrc
rm -rf gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2
```
* Create an alias for starting openocd
	* Add the following line to .bashrc
	* `alias f4_openocd="openocd -f interface/stlink-v2.cfg -f target/stm32f4x.cfg"

## Debugging
* First, connect the ST-Link to the board being debugged, and plug it into a USB port
* Run openocd
	* `$ f4_openocd`
	* I get the following output
```
~ $ f4_openocd 
Open On-Chip Debugger 0.10.0
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "hla_swd". To override use 'transport select <transport>'.
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
adapter speed: 2000 kHz
adapter_nsrst_delay: 100
none separate
Info : Unable to match requested speed 2000 kHz, using 1800 kHz
Info : Unable to match requested speed 2000 kHz, using 1800 kHz
Info : clock speed 1800 kHz
Info : STLINK v2 JTAG v17 API v2 SWIM v4 VID 0x0483 PID 0x3748
Info : using stlink api v2
Info : Target voltage: 3.228458
Info : stm32f4x.cpu: hardware has 6 breakpoints, 4 watchpoints
```
* Compile the program to be debugged (if it hasn't been already)
* In a separate terminal run GDB on the program to debug. Note: From what I can tell, it is important to make sure that GDB is started in the
directory containing `main.cpp`, otherwise it can't find the c++ code being executed on a line.
	* `$ arm-none-eabi-gdb obj/blink.elf`
* Connect to the openocd gdb server
	* `(gdb) target remote localhost:3333`
	* It seems that openocd defaults to port 3333, but to see what ports are being used run `$ netstat -nptl`
* Reset the board (honestly, I'm not sure what this is doing)
	* `(gdb) monitor reset halt`
* Load the program
	* `(gdb) load`
* Run the program
	* `(gdb) continue`
* For the above GDB steps, I get the following output
```
$ arm-none-eabi-gdb obj/blink.elf 
GNU gdb (GNU Tools for ARM Embedded Processors) 7.10.1.20160923-cvs
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "--host=i686-linux-gnu --target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from obj/blink.elf...done.
(gdb) target remote localhost:3333
Remote debugging using localhost:3333
0x080003de in __udivmoddi4 ()
(gdb) monitor reset halt
adapter speed: 2000 kHz
target halted due to debug-request, current mode: Thread 
xPSR: 0x01000000 pc: 0x08001560 msp: 0x20020000
(gdb) load
Loading section .isr_vector, size 0x188 lma 0x8000000
Loading section .text, size 0x2f68 lma 0x8000188
Loading section .ARM.extab, size 0x48 lma 0x80030f0
Loading section .ARM, size 0x100 lma 0x8003138
Loading section .init_array, size 0x4 lma 0x8003238
Loading section .fini_array, size 0x4 lma 0x800323c
Loading section .data, size 0xa8 lma 0x8003240
Start address 0x8001560, load size 13032
Transfer rate: 14 KB/sec, 1861 bytes/write.
(gdb) continue
Continuing.
```

After this, debugging is done using normal GDB commands, which are just a google search away.

