import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering


relay = 25

GPIO.setup(relay,GPIO.OUT)

while True:
	choice = int(raw_input("Choice:  1. for start or 2. for stop: "))
	if choice == 1:
		GPIO.output(relay, True)
	elif choice == 2:
		GPIO.output(relay, False)
	else:
		print 'Try again!'