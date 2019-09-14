#! /usr/bin/env python3

from pyftdi.i2c import *

DEV_ADDR = 0x21

REG_IODIR = 0x00
REG_IPOL = 0x01
REG_GPINTEN = 0x02
REG_DEFVAL = 0x03
REG_INTCON = 0x04
REG_IOCON = 0x05
REG_GPPU = 0x06
REG_INTF = 0x07
REG_INTCAP = 0x08
REG_GPIO = 0x09
REG_OLAT = 0x0A



#### From Tutorial ####
# Modified to work with FT232H board from Adafruit
# http://eblot.github.io/pyftdi/api/i2c.html

# Instantiate an I2C controller
i2c = I2cController()

# Configure the first interface (IF/1) of the FTDI device as an I2C master
i2c.configure('ftdi://ftdi:232h/1')

# Get a port to an I2C slave device
slave = i2c.get_port(DEV_ADDR)

# Write a register to the I2C slave
# set gpio0-3 as outputs and gpio(4:7) as inputs
slave.write_to(REG_IODIR, b'\xF0')

slave.write_to(REG_GPIO, b'\x05')

# Read a register from the I2C slave
gpio = slave.read_from(REG_GPIO, 1)
print("gpio = ", gpio)
