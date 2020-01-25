import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN=14
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

usercount = 0

def MOTION(PIR_PIN):
	print "Motion Detected"
	global usercount
	usercount = usercount + 1
	print "Current Usercount",usercount

print "PIR Module Test"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(PIR_PIN,GPIO.RISING,callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print "Quit. Final user count: ",usercount
	GPIO.cleanup()
