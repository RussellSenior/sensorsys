#!/usr/bin/python

import zmq
import time
import os
import string
import sys

if len(sys.argv) < 2:
	print("usage: %s <host>" % sys.argv[0])
	sys.exit(0)

syspath = "/sys/devices/platform/ocp/44e0d000.tscadc/TI-am335x-adc/iio:device0/in_voltage5_raw"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

while True:
	file = open(syspath,"r")
	content = file.read().rstrip()
	file.close()
	socket.send_string("%i %s %s" % (time.time(),"photoresistor",content))
	time.sleep(2)
