#!/bin/sh

stdbuf -o L /home/russell/src/rtl_433/src/rtl_433 -F csv | awk -W interactive '$0 != last { print $0 ; last = $0 }' | awk -W interactive -F, '$4 ~ /Acurite tower sensor/ { print $1,"acu-" $6 "-temp",$9 ; print $1,"acu-" $6 "-rh",$12 } $4 ~ /OSv1 Temperature Sensor/ { print $1,"os-" $121 "-temp",$9 }' | python /home/russell/src/sensorsys/sensor-pub.py dodson
