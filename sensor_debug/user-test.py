import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
MCW_PIN=14
PIR_PIN = 18
PIRM_PIN = 15

GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIRM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mcwusercount = 0
pirusercount = 0
pirmusercount = 0

def MCWMOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"
	global mcwusercount
	mcwusercount = mcwusercount + 1
	print "Current Microwave Usercount",mcwusercount

def PIRMOTION(PIR_PIN):
	print "Motion Detected by PIR Sensor"
	global pirusercount
	pirusercount = pirusercount + 1
	print "Current PIR Usercount",pirusercount

def PIRMMOTION(PIRM_PIN):
	print "Motion Detected by Modified PIR Sensor"
	global pirmusercount
	pirmusercount = pirmusercount + 1
	print "Current Modified PIR Usercount",pirmusercount

print "User Count Module Test"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MCWMOTION)
	GPIO.add_event_detect(PIR_PIN,GPIO.RISING,callback=PIRMOTION)
	GPIO.add_event_detect(PIRM_PIN,GPIO.RISING,callback=PIRMMOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print "Quit."
	print " Final Microwave user count: ",mcwusercount
	print " Final PIR user count: ",pirusercount
	print " Final Modified PIR user count: ",pirmusercount
	GPIO.cleanup()
