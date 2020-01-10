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

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get visible illuminance from BH1750 using I2C 0x23
# code from https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bh1750.py
# MAKE SURE TO ENABLE I2C IN RPi-config

# Define some constants from the datasheet
BHSEN     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x21 #Measurement at 0.5lux resolution
 
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
 
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=BHSEN):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  return convertToNumber(data)
 
print "Light Level : " + str(readLight()) + " lux"


