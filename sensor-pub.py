#!/usr/bin/python

import zmq
import sys

if len(sys.argv) < 2:
	print("usage: %s <host>" % sys.argv[0])
	sys.exit(0)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

while 1:
	line = sys.stdin.readline()
	if not line:
		break
	l = line.rstrip()
	print(l)
	socket.send_string("%s" % l)

