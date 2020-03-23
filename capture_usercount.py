import RPi.GPIO as GPIO
import time, datetime
import config
import threading
import mysql.connector

GPIO.setmode(GPIO.BCM)
MCW_PIN=14

GPIO.setup(MCW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def MCWMOTION(MCW_PIN):
	print "Motion Detected by Microwave Sensor"

	htimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	insertval = (htimestamp,config.sensor_id)
	insertquery = "INSERT INTO usercount (tstamp, sensorid) VALUES (%s, %s)",insertval

	dbconnect = mysql.connector.connect(host=config.db_host,user=config.db_user,password=config.db_password,database=config.db_name)

	cursor = dbconnect.cursor()
	cursor.execute(*insertquery)	
	dbconnect.commit()
	print(cursor.rowcount, "Record succesfully inserted into usercount table")
	cursor.close()
	dbconnect.close()

GPIO.add_event_detect(MCW_PIN,GPIO.RISING,callback=MCWMOTION)

print "User Count Module Test"
time.sleep(2)
print "Monitoring user count"
