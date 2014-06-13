#!/usr/bin/env python2
import smbus
from time import sleep

#############
# CONSTANTS #
#############
# IO (Input/Ouput) direction register address
IODIRA = 0x00
IODIRB = 0x01

# GPIO (General purpose input/output) register (the values of the pins)
GPIOA = 0x12
GPIOB = 0x13
OLATA = 0x14
OLATB = 0x15

# Variable declarations
bus = smbus.SMBus(1)
device_address = 0x20
delay = 0.8



def set_up_slice_of_pi():
	bus.write_byte_data(device_address, IODIRB, 0)

def turn_led_on():
	bus.write_byte_data(device_address, GPIOB, 1)

def turn_led_off():
	bus.write_byte_data(device_address, GPIOB, 0)

def flash_led():
	turn_led_on()
	print "Turning LED on"
	sleep(delay)
	turn_led_off()
	print "Turning LED off"
	sleep(delay)

set_up_slice_of_pi()
while True:
	flash_led()
