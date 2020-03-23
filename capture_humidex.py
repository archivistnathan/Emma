# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Test functionality of temperature and humidity sensor HTU21D
#
# FOR DEBUGGING ONLY
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

#!/usr/bin/python
import config
import smbus
import time, datetime
import mysql.connector
 
# Get I2C bus
bus = smbus.SMBus(1)
 
# SHT31 address, 0x44(68)
bus.write_i2c_block_data(0x44, 0x2C, [0x06])
 
time.sleep(0.5)
 
# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(0x44, 0x00, 6)
 
# Convert the data
rawtemp = data[0] * 256 + data[1]
ctemp = -45 + (175 * rawtemp / 65535.0)
hum = 100 * (data[3] * 256 + data[4]) / 65535.0

ctemp = round(ctemp,2)
hum = round(hum,2)
 
htimestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print "Temp: " + str(ctemp) + " deg C | Hum: " + str(hum) + " %RH | " + htimestamp + " Sensor " + str(config.sensor_id)

insertval = (str(ctemp),str(hum),htimestamp,config.sensor_id)
insertquery = "INSERT INTO humidex (temp, hum, tstamp, sensorid) VALUES (%s, %s, %s, %s)",insertval

config.dbinsert(insertquery)