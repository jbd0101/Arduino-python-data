
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import serial
import urllib2

ser = serial.Serial('/dev/ttyACM0', 9600)
base = "http://localhost:8000/LoadDatas?data=true"
data =""
debut = "non-defini"

derniere_maj=0
isline=False
def sendData(data,m):
	global derniere_maj
	if derniere_maj+(60) < m:
		url = base+data
		try:
			response = urllib2.urlopen(url)
			html = response.read()
			derniere_maj = m
			print html
			return True
		except:
			print "erreur"
			return False
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
		sendData(data,m)
		isline=True

	try:
		if line[0] != "#" and debut != "non-defini" and isline==False:
			line = line.split(":")
			data +="&"+line[0]+"="+str(line[1])
	except:
		debut  = "non-defini"
		data = ""

