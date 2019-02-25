#import libraries we will use
import Adafruit_DHT

#Assign GPIO pins
tempPin = 17

# Temp and humidity sensor
tempSensor = Adafruit_DHT.DHT22


while True:

	print "running"
	# change back to passing varibles
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	print "\t set hum and temp"
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
#		tempFahr = '{0:0.1f}*F'.format(temperature)
		print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temperature, humidity))
	else:
		print('Failed to get reading! Try again!')
