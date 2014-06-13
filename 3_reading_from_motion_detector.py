#!/usr/bin/env python2
import smbus
from time import sleep

#############
# CONSTANTS #
#############
# IO (Input/Ouput) direction register address
IODIRA = 0x00
IODIRB = 0x01

# GPIO (General purpose input/output) register (the values of the pins as inputs)
GPIOA = 0x12
GPIOB = 0x13
OLATA = 0x14
OLATB = 0x15

# Variable declarations
bus = smbus.SMBus(1)
device_address = 0x20
delay = 0.8

def setup_slice_of_pi():
	setup_outputs()

def setup_outputs():
	bus.write_byte_data(device_address, IODIRA, 0b00000010)
	bus.write_byte_data(device_address, GPIOA, 0b00000001)

def turn_on_pin_on_port_a(pin_num):
	bus.write_byte_data(device_address, GPIOA, 1 << (pin_num - 1))
	
def read_from_sensor():
	return (bus.read_byte_data(device_address, GPIOA) >> 1)

setup_slice_of_pi()
while True:
	print read_from_sensor()
	sleep(0.1)

