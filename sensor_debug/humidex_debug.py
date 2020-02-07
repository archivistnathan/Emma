# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Test functionality of temperature and humidity sensors
#
# FOR DEBUGGING ONLY
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# import libraries for GPIO and I2C
import os
import glob
import smbus
import time
import Adafruit_DHT

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get DS18B20 temperature using one-wire
# REMEMBER TO ENABLE ONE-WIRE IN RPi-config

# Initialize the GPIO Pins
os.system('modprobe w1-gpio')  # Turns on the GPIO module
os.system('modprobe w1-therm') # Turns on the Temperature module
 
# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
# A function that reads the sensors data
def read_temp_raw():
	f = open(device_file, 'r') # Opens the temperature device file
	lines = f.readlines() # Returns the text
	f.close()
	return lines
  
lines = read_temp_raw() # Read the temperature 'device file'
 
# While the first line does not contain 'YES', wait for 0.2s
# and then read the device file again.
while lines[0].strip()[-3:] != 'YES':
	time.sleep(0.2)
	lines = read_temp_raw()
 
# Look for the position of the '=' in the second line of the
# device file.
equals_pos = lines[1].find('t=')
 
# If the '=' is found, convert the rest of the line after the
# '=' into degrees Celsius and store in dstemp
if equals_pos != -1:
	temp_string = lines[1][equals_pos+2:]
	dstemp = float(temp_string)/1000
    
# Print to screen
print "Temperature from DS18B20 is    : %.2f C" %dstemp

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get MCP9808 temperature using I2C 0x18
# code from https://github.com/DcubeTechVentures/MCP9808/blob/master/Python/MCP9808.py
# MAKE SURE TO ENABLE I2C IN RPi-config

# Get I2C bus
bus = smbus.SMBus(1)
# MCP9808 address, 0x18(24)
# Select configuration register, 0x01(1)
#		0x0000(00)	Continuous conversion mode, Power-up default
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
# MCP9808 address, 0x18(24)
# Select resolution rgister, 0x08(8)
#		0x03(03)	Resolution = +0.0625 / C
bus.write_byte_data(0x18, 0x08, 0x03)

time.sleep(0.5)

# MCP9808 address, 0x18(24)
# Read data back from 0x05(5), 2 bytes
# Temp MSB, TEMP LSB
data = bus.read_i2c_block_data(0x18, 0x05, 2)

# Convert the data to 13-bits
mcptemp = ((data[0] & 0x1F) * 256) + data[1]

print "MCP9808 Raw Temperature Data: ", str(bin(mcptemp))[2:]

if mcptemp > 4095 :
	mcptemp -= 8192
mcptemp = mcptemp * 0.0625

trytemp = (256-mcptemp)/10
print "Positive Temperature Attempt is    : %.4f C" %trytemp

# Output data to screen
print "Temperature from MCP9808 is    : %.2f C" %mcptemp

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get DHT22 temperature and humidity using proprietary one-wire via Adafruit library

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17

dhthum, dhttemp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if dhthum is not None and dhttemp is not None:
	print "Temperature from DHT22 is    : %.1f C" %dhttemp
	print "Humidity from DHT22 is    : %.1f RH" %dhthum
else:
	print("Failed to retrieve data from DHT22")

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get HTU21D/SHT21 temperature and humidity using I2C 0x40
# code from https://github.com/jasiek/HTU21D/blob/master/HTU21D.py

I2C_ADDR = 0x40
CMD_TRIG_TEMP_HM = 0xE3
CMD_TRIG_HUMID_HM = 0xE5
CMD_TRIG_TEMP_NHM = 0xF3
CMD_TRIG_HUMID_NHM = 0xF5
CMD_WRITE_USER_REG = 0xE6
CMD_READ_USER_REG = 0xE7
CMD_RESET = 0xFE
    
class HTU21D:
	def __init__(self, busno):
		self.bus = smbus.SMBus(busno)

	def read_temperature(self):
		self.reset()
		msb, lsb, crc = self.bus.read_i2c_block_data(I2C_ADDR, CMD_TRIG_TEMP_HM, 3)
		return -46.85 + 175.72 * (msb * 256 + lsb) / 65536
     
	def read_humidity(self):
		self.reset()
		msb, lsb, crc = self.bus.read_i2c_block_data(I2C_ADDR, CMD_TRIG_HUMID_HM, 3)
		return -6 + 125 * (msb * 256 + lsb) / 65536.0

	def reset(self):
		self.bus.write_byte(I2C_ADDR, CMD_RESET)

if __name__ == '__main__':
	htu = HTU21D(1)
	htutemp = htu.read_temperature()
	htuhum = htu.read_humidity()
	print "Temperature from HTU21D is    : %.2f C" %htutemp
	print "Humidity from HTU21D is    : %.2f RH" %htuhum

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get SHT31 temperature and humidity using I2C 0x44
# code from http://www.pibits.net/code/raspberry-pi-sht31-sensor-example.php

# SHT31 address, 0x44(68), bus already declared in MCP9808 section
bus.write_i2c_block_data(0x44, 0x2C, [0x06])
 
time.sleep(0.5)
 
# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(0x44, 0x00, 6)
 
# Convert the data
temp = data[0] * 256 + data[1]
cTemp = -45 + (175 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
 
# Output data to screen
print "Temperature in Celsius is : %.3f C" %cTemp
print "Relative Humidity is : %.2f %%RH" %humidity

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# validate readings by redundant comparison

# checks temperature readings are within 0.3 deg C of each other
# focuses on value from MCP9008 as sensor with highest accuracy according to datasheet
htudsdiff = abs(htutemp - dstemp)
htudhtdiff = abs(htutemp - dhttemp)
htumcpdiff = abs(htutemp - mcptemp)
if ((abs(htutemp - dstemp) < 0.3) or (abs(htutemp - dhttemp) < 0.3) or (abs(htutemp - mcptemp) < 0.3)):
	print "Verified temperature is %.2f deg C" %htutemp
#elif (((abs(htutemp - dstemp) < 0.3) and (abs(htutemp - dhttemp) < 0.3)):
#	print "Failsafe verified temperature is %.2f deg C" %htutemp
else:
	print "Temperature Reading Mismatch: htudsdiff %.2f"  %htudsdiff+" htudhtdiff %.2f" %htudhtdiff+" htumcpdiff %.2f" %htumcpdiff

# check humidity readings are within 3%RH of each other
# selects value from HTU21D as sensor with highest consistent accuracy
humdiff = abs(htuhum - dhthum)
if (abs(htuhum - dhthum) < 5):
	print "Verified humidity is %.2f RH" %htuhum
else:
	print "Humidity Reading Mismatch: difference is %.2f" %humdiff

# return valid reading from most accurate sensor
