import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor = 21

 
GPIO.setup(Motor,GPIO.OUT)

print "Turning motor on"
sleep(2)
GPIO.output(Motor,GPIO.HIGH)
sleep(2) 
print "Stopping motor"
GPIO.output(Motor,GPIO.LOW) 
GPIO.cleanup()
