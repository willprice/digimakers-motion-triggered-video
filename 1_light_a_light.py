#!/usr/bin/env python2
import smbus
from time import sleep
#########
# NOTES #
#########

# The line above is read by the shell/command line which determines whether the
# code should be run as a shell script, or by another program. In this case
# since we're developing a python program, we want it to be interpreted using
# python, specifically python2 (this is the same as doing `python2
# script_name.py`). 

# We're going to use a Slice of PI/O expansion board instead of using the GPIO
# pins, this has multiple benefits, in particular:
# - The raspberry pi is protected so if you connect something up wrong, you've
#   broken a cheap chip instead of an expensive Pi!
# - You can chain multiple Slice of PI/O boards together to get a whole bunch of
#   input/output devices (imagine you want to control 40 LEDs on a christmas
#   tree)

# Using a Slice of PI/O expansion board is a little more difficult than just
# using the GPIO pins if we have to set up the device to use it, and ask for the
# values of specific pins. The RPi's GPIO is configured in the same way, but
# someone has written a 'wrapper' around this to make life easier for you.
# Wrappers are just bits of code that make something easier to use. In this case
# the RPi's GPIO python interface is a wrapper around the registers of the ARM
# processor on the RPi. A register is a block of storage that is usually
# manipulated using binary. Here we're going to configure the Slice of
# PI/O using binary operations.

# Hexademical is a system of numbering where each digit ranges from 0-F (0-15 in
# decimal), it corresponds quite nicely to binary since each digit can be
# represented as 4 bits (don't worry if you don't understand, but it may be nice
# to have a play around converting between binary and hexadecimal).


#############
# CONSTANTS #
#############

# IO (Input/Ouput) direction register address
IODIRA = 0x00
IODIRB = 0x01

# GPIO (General purpose input/output) register (the values of the pins)
GPIOA = 0x12
GPIOB = 0x13

##########
# SET UP #
##########
# On power up the device is configured like so:
# IODIRA == 0b00000000
# IODIRB == 0b00000000
# Each bit of the IODIRx register represents a pin's direction.
# 0 means that the pin acts as an output
# 1 means that the pin acts as an input
# GPIOA  == 0b00000000
# GPIOB  == 0b00000000
# So by default, all the pins are set as outputs, set at 0v.
# We want to turn B0 off and on. It's direction in the IODIRB register is
# correct, but we need to turn it on by manipulating the GPIOB register.
bus = smbus.SMBus(1)
device_address = 0x20
bus.write_byte_data(device_address, IODIRB, 0)
while True:
	bus.write_byte_data(device_address, GPIOB, 1)
	sleep(0.5)
	bus.write_byte_data(device_address, GPIOB, 0)
	sleep(0.5)

