#Import libraries
import RPi.GPIO as GPIO
import time
import os

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#This function will make the light blink once
def blinkOnce (pin) :
	GPIO.output(pin, True)
	time.sleep(.1)
	GPIO.output(pin, False)
	time.sleep(.1)

#Call the blinkOnce function above in a loop
#for i in range(10):
#	blinkOnce(17)

try:
	while True:
		input_state = GPIO.input(26)
		if input_state == False:
			for i in range(10) :
				blinkOnce(17)
			time.sleep(.2)

#Cleanup the GPIO when done
#GPIO.cleanup()

except KeyboardInterrupt :
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
