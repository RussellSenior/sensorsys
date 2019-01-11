import sys
import zmq
import signal
import io
import os
import os.path

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

logfname = 'incoming.log'
newfname = 'rotated.log'
printed = False

if os.path.isfile(logfname):
	if os.stat(logfname).st_size > 0:
		printed = True

logfile = io.open(logfname,'a')

closeFlag = False
printing = False

def rotateLog():
	global printed
	global logfile
	global closeFlag

	if printed:
		logfile.close()
		os.rename(logfname,newfname)
		logfile = open(logfname,"w")
	closeFlag = False

def handleHUP(signalNumber, frame):
	global printing
	global closeFlag

	if printing:
		closeFlag = True
	else:
		rotateLog()

signal.signal(signal.SIGHUP, handleHUP)

print("Collecting updates from sensor servers")
socket.bind("tcp://*:5556")

socket.setsockopt(zmq.SUBSCRIBE, b'')

# Process incoming messages
while True:
	string = socket.recv_string()
	printing = True
	logfile.write(string + "\n")
	logfile.flush()
	printed = True
	print("received: %s" % (string))
	printing = False
	if closeFlag:
		rotateLog()

