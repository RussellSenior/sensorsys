#!/usr/bin/python

import zmq
import time
import os
import string
import sys

if len(sys.argv) < 3:
	print("usage: %s <host> <w1_bus_master_number>" % sys.argv[0])
	sys.exit(0)

syspath = "/sys/bus/w1/devices/w1_bus_master" + sys.argv[2] + "/"

print("iterating on devices on %s" % syspath)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

while True:
	count = 0
	for filename in os.listdir(syspath):
		if filename.startswith("28-"):
			fullfname = syspath + filename + "/w1_slave"
			file = open(fullfname,"r")
			content = file.read()
			file.close()
			lines = content.split("\n")
			fields = lines[0].split()
			crc_ok = (fields[11] == "YES")
			fields = lines[1].split("=")
			temp_c = fields[1]
			# print("%s %s %i" % (filename,temp_c,crc_ok))
			if crc_ok:
				socket.send_string("%i %s %s" % (time.time(),filename,temp_c))
			count = count + 1
	if count == 0:
		time.sleep(5)	
