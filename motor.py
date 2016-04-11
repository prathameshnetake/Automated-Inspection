import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor = 21 
GPIO.setup(Motor,GPIO.OUT)


def motorControl(ip):
	if ip == 1:
		print "****  Turning motor on  ****"
		sleep(0.5)
		GPIO.output(Motor, GPIO.HIGH)
		sleep(0.5)
	elif ip == 0:
		sleep(0.5)
		print "****  Stopping motor ****"
		GPIO.output(Motor, GPIO.LOW) 
		sleep(0.5)
	else:
		print " *****  Invalid signal  **** "	

if __name__ == "__main__":
	while True:
        	ip = int(raw_input("Choice 1.Turn On relay 0. Turn off relay"))
        	motorControl(ip)


	GPIO.cleanup()
	
