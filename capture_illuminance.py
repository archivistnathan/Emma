# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Test functionality of visible illuminance and UV sensors
#
# FOR DEBUGGING ONLY
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# import libraries for GPIO and I2C
import smbus
import time
import os

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get visible illuminance from BH1750 using I2C 0x23
# code derived from https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bh1750.py and http://www.pibits.net/code/raspberry-pi-bh1750-light-sensor.php
# MAKE SURE TO ENABLE I2C IN RPi-config

# Define some constants from the datasheet
BHSEN     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
CON_HIGH_RES_MODE = 0x11 # Continuous Measurement at 0.5lux resolution
ONE_TIME_HIGH_RES_MODE = 0x21 # Measurement at 0.5lux resolution
 
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

bus.write_byte(BHSEN,POWER_ON)
time.sleep(0.5)
bus.read_i2c_block_data(BHSEN,CON_HIGH_RES_MODE)
time.sleep(0.5)
 
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=BHSEN):
  # bus.write_byte(addr,POWER_ON)
  data = bus.read_i2c_block_data(addr,CON_HIGH_RES_MODE)
  return convertToNumber(data)

print "BH1750 Light Level : " + str(readLight()) + " lux"

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get uv illuminance from VEML6070 using I2C 0x38 and 0x39
# code derived from http://www.pibits.net/code/raspberry-pi-and-veml6070-sensor-example.php
# MAKE SURE TO ENABLE I2C IN RPi-config

# I2C address of the device
VEML6070_DEFAULT_ADDRESS				= 0x38
 
# VEML6070 Command Set
VEML6070_CMD_ACK_DISABLE				= 0x00 # Acknowledge Disable
VEML6070_CMD_ACK_ENABLE					= 0x20 # Acknowledge Enable
VEML6070_CMD_ACK_THD_102				= 0x00 # Acknowledge threshold 102 Steps
VEML6070_CMD_ACK_THD_145				= 0x10 # Acknowledge threshold 145 Steps
VEML6070_CMD_IT_1_2T					= 0x00 # Integration time = 1/2T
VEML6070_CMD_IT_1T						= 0x04 # Integration time = 1T
VEML6070_CMD_IT_2T						= 0x08 # Integration time = 2T
VEML6070_CMD_IT_4T						= 0x0C # Integration time = 4T
VEML6070_CMD_RESERVED					= 0x02 # Reserved, Set to 1
VEML6070_CMD_SD_DISABLE					= 0x00 # Shut-down Disable
VEML6070_CMD_SD_ENABLE					= 0x01 # Shut-down Enable
VEML6070_CMD_READ_LSB					= 0x38 # Read LSB of the data
VEML6070_CMD_READ_MSB					= 0x39 # Read MSB of the data
 
class VEML6070():
	def __init__(self):
		self.write_command()
 
	def write_command(self):
		"""Select the UV light command from the given provided values"""
		COMMAND_CONFIG = (VEML6070_CMD_IT_4T)
		bus.write_byte(VEML6070_DEFAULT_ADDRESS, COMMAND_CONFIG)
 
	def read_uvlight(self):
		"""Read data back VEML6070_CMD_READ_MSB(0x73) and VEML6070_CMD_READ_LSB(0x71), uvlight MSB, uvlight LSB"""
		data0 = bus.read_byte(VEML6070_CMD_READ_MSB)
		data1 = bus.read_byte(VEML6070_CMD_READ_LSB)
 
		# Convert the data
		uvlight = float(data0 * 256 + data1)
 
		return {'u' : uvlight}
 
veml6070 = VEML6070()

veml6070.write_command() 
light = veml6070.read_uvlight()
print "UV Light Level : %d" %(light['u'])