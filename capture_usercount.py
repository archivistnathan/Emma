import RPi.GPIO as GPIO
import time, datetime
import config

GPIO.setmode(GPIO.BCM)
MCW_PIN=14

GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def MCWMOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"

	htimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	insertval = (htimestamp,config.sensor_id)
	insertquery = "INSERT INTO usercount (tstamp, sensorid) VALUES (%s, %s)",insertval

	config.dbinsert(insertquery)

GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MCWMOTION)

print "Initiating User Count Module"
time.sleep(2)
print "Monitoring user count"
