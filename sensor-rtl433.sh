#!/bin/sh

stdbuf -o L /home/russell/src/rtl_433/src/rtl_433 -F csv -M newmodel | awk -W interactive '$0 != last { print $0 ; last = $0 }' | awk -W interactive -F, '$4 ~ /Acurite-Tower/ { print $1,"acu-" $6 "-temp",$9 ; print $1,"acu-" $6 "-rh",$13 } $4 ~ /Oregon-v1/ { print $1,"os-" $6 "-temp",$9 }' | awk -W interactive 'NF == 3' | /home/russell/src/sensorsys/sensor-pub.py dodson
