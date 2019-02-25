#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import time
import sqlite3 as mydb
import sys

#assign my pins
greenPin = 17
redPin = 13

#init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)

#LED vars
#blink duration
blinkDur = .1

curTemp = 50

"""Log Curr Time, temp in celsius and fahrenheit to an sqlite3 database"""

def readTemp():
	global curTemp
	tempfile = open("/sys/bus/w1/devices/28-0000069616c4/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime("%x %X %Z")
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	curTemp = tempF
	return [currentTime, tempC, tempF]

con = mydb.connect('/home/lisaisfabu/ELSpring2019/code/temperature.db')
cur = con.cursor()

def logTemp():
	with con:
		try:
			[t,C,F] = readTemp()
			print "Current Temperature is: %s F" %F
			#sql = "insert into tempData values(?,?,?)"
			cur.execute('insert into TempData values(?,?,?)', (t,C,F))
			print "Temperature logged"
		except:
			print "Error!!"

def print_table():
	table = con.execute("select * from TempData")
	os.system('clear')
	for row in table:
		print row

def blink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def every_min_read():
	i = 0
	oldTime = 60

	while True:
		if (time.time() - oldTime) > 59:
			logTemp()
			print_table()
			old_time = time.time()
		if curTemp >= 68 and curTemp <= 78:
			GPIO.output(greenPin,True)
		else:
			GPIO.output(greenPin,False)
			blink(redPin)

		i += 1
try:
	every_min_read()
	GPIO.cleanup()

except KeyboardInterrupt:
	os.system('clear')
	print('Bobagump')
	GPIO.cleanup()
