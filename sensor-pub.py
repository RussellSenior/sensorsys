#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#

import zmq
import time;

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5556")

while True:
	socket.send_string("%i 1" % (time.time()))
	time.sleep(2)
