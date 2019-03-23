#importing lib i'm using
import RPi.GPIO as GPIO
import time
import os
import sqlite3 as mydb

#assign my pins
enterPin = 13
exitPin = 26

#init my GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(enterPin, GPIO.IN)
GPIO.setup(exitPin, GPIO.IN)

#connect to my db and have a cursor to my db
con = mydb.connect('/home/lisaisfabu/ELSpring2019/code/motion/motion.db')
cur = con.cursor()

counter = 0
enter = 0
out = 0

def readCounter():
    global counter
    global enter
    global out

    if GPIO.input(exitPin):
        currentTimeOut = time.strftime("%x %X %Z")
        currentTimeIn = 0
        out = out + 1
        counter = counter - 1
    elif GPIO.input(enterPin):
        currentTimeIn = time.strftime("%x %X %Z")
        currentTimeOut = 0
        enter = enter + 1
        counter = counter + 1
    return [currentTimeIn, enter, currentTimeOut, out, counter]

def logPeople():
    with con:
        try:
            [i,e,c,o,t] = readCounter()
            print "time %s" %i
            cur.execute('insert into inAndOut values(?,?,?,?,?)', (i,e,c,o,t))
            print "person logged"
        except:
            print "error!"

def logCounter():
    global counter 

    time.sleep(10)
    while True:
        if GPIO.input(exitPin):
            logPeople()
            print("out " + str(counter))
            time.sleep(4)
        elif GPIO.input(enterPin):
            logPeople()
            print("in " + str(counter))
            time.sleep(4)

try:
    logCounter()
    GPIO.cleanup()
    
except KeyboardInterrupt:
    os.system('clear')
    con.close()
    print(counter)
    GPIO.cleanup()
