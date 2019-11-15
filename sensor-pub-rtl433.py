#!/usr/bin/python

import subprocess
import zmq
import sys

if len(sys.argv) < 2:
	print("usage: %s <host>" % sys.argv[0])
	sys.exit(0)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://" + sys.argv[1] + ":5556")

rtl = subprocess.Popen(['/home/russell/src/rtl_433/build/src/rtl_433', '-Fcsv', '-Mnewmodel' , '-Mtime:unix', '-R50', '-R40'], stdout=subprocess.PIPE)

k = rtl.stdout.readline()
ka = k.rstrip().split(",")

# time
# msg
# codes
# brand 
# model 
# sid 
# id 
# channel 
# battery_ok 
# temperature_C 
# subtype 
# message_type
# sensor_id
# sequence_num
# battery_low
# temperature_F
# humidity
# wind_speed_mph
# wind_speed_kph
# wind_avg_mi_h
# wind_avg_km_h
# wind_dir_deg
# rain_inch
# rain_in
# rain_mm

last = ''
previous = { }
delta = 5
v = [ ka.index(i) for i in ka if i in ("time","brand","model","id","channel","battery_ok","temperature_C","humidity") ]


while True:
	d = rtl.stdout.readline()
	da = d.rstrip().split(",")
	(time,brand,model,id,channel,battery_ok,temperature_C,humidity) = [ da[i] for i in v ]
	if (id not in previous) or (int(time) > (previous[id] + delta)):
		print time,brand,model,id,channel,battery_ok,temperature_C,humidity
		if model == "Acurite-Tower":
			socket.send_string("%s %s %s" % (time,"acu-" + id + "-temp", temperature_C))
			socket.send_string("%s %s %s" % (time,"acu-" + id + "-rh", humidity))
		elif model == "Oregon-v1":
			socket.send_string("%s %s %s" % (time,"os-" + id + "-temp", temperature_C))
	previous[id] = int(time)
