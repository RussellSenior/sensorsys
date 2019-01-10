import zmq
import time
import os
import string
import sys

if len(sys.argv) < 2:
	print("usage: %s <host>" % sys.argv[0])
	sys.exit(0)

syspath = "/sys/bus/i2c/devices/2-0076/iio:device1/"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

def fetch_bme280(filename,label):
	fullfname = syspath + filename
	file = open(fullfname,"r")
	content = file.read().rstrip()
	file.close()
	socket.send_string("%i %s %s" % (time.time(),"bme280-" + label,content))

while True:
	fetch_bme280("in_humidityrelative_input","rh")
	fetch_bme280("in_pressure_input","bp")
	fetch_bme280("in_temp_input","temp")
	time.sleep(2)

