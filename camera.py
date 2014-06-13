#!/usr/bin/env python2
import smbus
from time import sleep
import picamera
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
bus = smbus.SMBus(1)
device_address = 0x20
bus.write_byte_data(device_address, IODIRA, 0x01)
bus.write_byte_data(device_address, IODIRB, 0x00)
bus.write_byte_data(device_address, GPIOB, 0x01)

print "Stabilising reading from motion sensor, please wait"
sleep(10)

with picamera.PiCamera() as camera:
	prev_triggered = False
	while True:
		triggered = bus.read_byte_data(device_address, GPIOA) & 1
		sleep(0.1)
		if triggered and not prev_triggered:
			camera.start_preview()
			prev_triggered = True
		elif not triggered and prev_triggered:
			camera.stop_preview()
			prev_triggered = False

