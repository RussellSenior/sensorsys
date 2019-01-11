import zmq
import sys

if len(sys.argv) < 2:
	print("usage: %s <host>" % sys.argv[0])
	sys.exit(0)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

for line in sys.stdin:
	l = line.rstrip()
	print(l)
	socket.send_string("%s" % l)

