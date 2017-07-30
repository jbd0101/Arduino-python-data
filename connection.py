
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
base = "http://localhost/LoadDatas?data=true"
data =""
debut = "non-defini"
derniere_maj = 0
isline=False
def sendData(data):
	print data
	return True
while 1 :
	line = ser.readline()
	line = line.strip()
	line = line.replace(" ","")
	m = time.localtime()
	m = time.mktime(m)
	isline=False
	if line=="debut":
		debut = True
		data = ""
		isline=True

	elif line=="fin":
		debut = False
		sendData(data)
		isline=True

	try:
		if line[0] != "#" and debut != "non-defini" and isline==False:
			line = line.split(":")
			derniere_maj = m
			data +="&"+line[0]+"="+str(line[1])
	except:
		debut  = "non-defini"
		data = ""
		print line
		print "erreur"

