import RPi.GPIO as GPIO
import time, datetime
import config
import threading

GPIO.setmode(GPIO.BCM)
MCW_PIN=14

GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def MCWMOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"

	htimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	insertval = (htimestamp,config.sensor_id)
	insertquery = "INSERT INTO usercount (tstamp, sensorid) VALUES (%s, %s)",insertval

	cursor = config.dbconnect.cursor()
	cursor.execute(*insertquery)	
	config.dbconnect.commit()
	print(cursor.rowcount, "Record succesfully inserted into usercount table")
	cursor.close()

def countingthread():
	GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MCWMOTION)
	while 1:
		time.sleep(100) #This prevents double readings, adjust for sensitivity

print "User Count Module Test"
time.sleep(2)
print "Monitoring user count"

thread = threading.Thread(target=countingthread)
thread.start()
