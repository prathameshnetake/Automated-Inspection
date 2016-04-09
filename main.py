import RPi.GPIO as GPIO
import time
import ultra    #this file will give current position of objects in cm
GPIO.setmode(GPIO.BCM)

print '############# Welcome to Main Program ##############'
print '############ Autonomous Object inspection ##########'


while True:
	pos = ultra.distance_in_cm()
	print pos 
	
