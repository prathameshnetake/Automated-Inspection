import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


#Pin configuration
MOTOR = 21
TRIG = 23
ECHO = 24

def distance_in_cm():
  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  #print "Waitng For Sensor To Settle"
  time.sleep(0.5)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    #print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    return distance - 0.5
  else:
    #print "Out Of Range"                   #display out of range
    return 0

def motorControl(ip):
	GPIO.setup(MOTOR,GPIO.OUT)
        if ip == 1:
                print "****  Turning motor on  ****"
                time.sleep(0.05)
                GPIO.output(MOTOR, True)
                time.sleep(0.05)
        elif ip == 0:                
                print "****  Stopping motor ****"
                time.sleep(0.05)
                GPIO.output(MOTOR, False)
                time.sleep(0.05)
        else:
                print " *****  Invalid signal  **** "

def setup():
	motorControl(1)


def makeMatch():
	print "Ooops! this function is not yet implemrnted"





def goodbye():
	print "\n\n\n\n **** Goodbye **** Stopping everything"
	motorControl(0)
	GPIO.cleanup()





print '############# Welcome to Main Program ##############'
print '############ Autonomous Object inspection ##########'

while True:
	choice = raw_input("Should i start the program?   (y/n)  :")
	if choice == 'y':
		break

try:
	while True:
		setup()	
		pos = distance_in_cm()
		print pos
		time.sleep(0.05)
		if pos > 13 and pos < 25:
			print "Object Fount!"
			print "Calculating center and Stopping main motor"
			
			motorControl(0)
			print "Motor is been stopped"
			time.sleep(3)
			print "Passing control to the make match funtion"
			makeMatch()
			print "Making match complete now reseting all the setup"

			setup()
		else:
			print "Waiting for object to come in front"
	 
except KeyboardInterrupt:
	goodbye()


