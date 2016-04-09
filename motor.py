import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor = 21 
GPIO.setup(Motor,GPIO.OUT)


def motorControl(ip):
	if ip == True:
		print "****  Turning motor on  ****"
		sleep(0.5)
		GPIO.output(Motor,GPIO.HIGH)
		sleep(5)
	elif ip == False:
		sleep(0.5)
		print "****  Stopping motor ****"
		GPIO.output(Motor,GPIO.LOW) 
	else:
		print " *****  Invalid signal  **** "
	GPIO.cleanup()


if __name__ == "__main__":
	motorControl(False)