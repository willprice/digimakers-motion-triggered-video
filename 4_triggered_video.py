#!/usr/bin/env python2
import smbus
from time import sleep
from Adafruit_MCP230xx import Adafruit_MCP230XX 
import picamera

counter = 0 
slice_of_pi = Adafruit_MCP230XX (0x20, 8)

def setup():
	slice_of_pi.config(0, Adafruit_MCP230XX.OUTPUT)
	slice_of_pi.config(7, Adafruit_MCP230XX.INPUT)
	slice_of_pi.output(0, 1)

def take_video():
	global counter
	counter += 1
	with picamera.PiCamera() as camera:
		camera.start_recording('pic_' + str(counter) + '.jpg')
		camera.start_preview()
		while triggered:
			triggered = read_sensor()
		camera.stop_preview()
		camera.stop_recording()

			

def read_sensor():
	return slice_of_pi.input(7)

setup()
while True:
	triggered = read_sensor()
	print triggered
	if triggered:
		take_video()

	sleep(1)
