#!/usr/bin/env python2
import smbus
from time import sleep
from Adafruit_MCP230xx import Adafruit_MCP230XX 
import picamera

counter = 0 
slice_of_pi = Adafruit_MCP230XX (0x20, 2)

def setup():
	slice_of_pi.config(0, Adafruit_MCP230XX.OUTPUT)
	slice_of_pi.output(0, 1)

def take_picture():
	global counter
	counter += 1
	with picamera.PiCamera() as camera:
		camera.capture('pic_' + str(counter) + '.jpg')

triggered = slice_of_pi.input(1)

setup()
take_picture()
