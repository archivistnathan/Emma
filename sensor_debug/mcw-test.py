import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
MCW_PIN=14
GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

usercount = 0

def MOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"
	global usercount
	usercount = usercount + 1
	print "Current Usercount",usercount

print "Microwave Module Test"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print "Quit. Final user count: ",usercount
	GPIO.cleanup()
