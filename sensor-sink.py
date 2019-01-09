#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from sensor servers")
socket.bind("tcp://*:5556")

socket.setsockopt(zmq.SUBSCRIBE, b'')

# Process incoming messages
while True:
	string = socket.recv_string()
	print("received: %s" % (string))

