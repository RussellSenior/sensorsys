#!/usr/bin/python

import sys
import os

topdir = "data"
f = { }

if not os.path.isdir(topdir):
	os.mkdir(topdir)

for line in sys.stdin:
	(time,sensor,rest) = line.rstrip().split(" ")
	# print(sensor,time,rest)
	sensorPath = topdir + "/" + sensor
	if not os.path.isdir(sensorPath):
		os.mkdir(sensorPath)
		os.link("mkstuff/Makefile",sensorPath + "/Makefile")
		os.link("mkstuff/multiplier.mk.1",sensorPath + "/multiplier.mk")
	day = int(time)
	day = day - (day % 86400)
	fname = sensorPath + "/" + ("%u" % day) + ".log"
	out = f.get(fname)
	if out == None:
		out = open(fname,"a+")
		f[fname] = out
		# print("opened %s for appending" % fname)
	out.write("%s %s\n" % (time,rest))

for fname in f:
	out = f[fname]
	out.close()
	print("closed %s" % fname)
