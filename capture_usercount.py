import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
MCW_PIN=14

GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mcwusercount = 0

def MCWMOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"
	global mcwusercount
	mcwusercount = mcwusercount + 1
	print "Current Microwave Usercount",mcwusercount

print "User Count Module Test"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MCWMOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print "Quit."
	print " Final Microwave user count: ",mcwusercount
	GPIO.cleanup()
