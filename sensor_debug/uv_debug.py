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
ONE_TIME_HIGH_RES_MODE = 0x21 #Measurement at 0.5lux resolution
 
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
 
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=BHSEN):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
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
		COMMAND_CONFIG = (VEML6070_CMD_ACK_DISABLE | VEML6070_CMD_IT_4T | VEML6070_CMD_SD_DISABLE | VEML6070_CMD_RESERVED)
		bus.write_byte(VEML6070_DEFAULT_ADDRESS, COMMAND_CONFIG)
 
	def read_uvlight(self):
		"""Read data back VEML6070_CMD_READ_MSB(0x73) and VEML6070_CMD_READ_LSB(0x71), uvlight MSB, uvlight LSB"""
		data0 = bus.read_byte(VEML6070_CMD_READ_MSB)
		data1 = bus.read_byte(VEML6070_CMD_READ_LSB)
 
		# Convert the data
		uvlight = float(data0 * 256 + data1)
 
		return {'u' : uvlight}
 
veml6070 = VEML6070()
 
light = veml6070.read_uvlight()
print "UV Light Level : %d" %(light['u'])
print " *********************************** "

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# get visible illuminance from Si1145 using I2C 0x60
# code derived from http://52.10.242.165/topic/139/python-code-for-si1145
# MAKE SURE TO ENABLE I2C IN RPi-config

#Convert unsigned to signed value

def signed(value):
        if value > 32767:
                value -= 65536
        return value

#Read value from internal addr from chip. chip is the actual I2C slave address and addr the internal address of the device

def read_address(chip,addr):
        l='i2cget -y 1 '+str(chip)+' '+str(addr)+' b'
        p = os.popen(l)
        s = p.readline()
        p.close()
        return s

#Read 2 byte(16b) from internal addr(addr,addr+1) from chip.


def read_word_data(chip,addr):
        lsb = int(read_address(chip,addr),0)
        msb = int(read_address(chip,addr+1),0)
        value = (msb << 8) + lsb
        return value


#Write data into the addr of chip. chip is the actual I2C slave address and addr the internal address of the device

def write_address(chip,addr,data):
        l='i2cset -y 1 '+str(chip)+' '+str(addr)+' '+str(data)+' b'
        p = os.popen(l)
        p.close()

#Read unsigned 8 bits from internal addr of chip. chip is the actual I2C slave address and addr the internal address of the $


def readU8(chip,addr):
        result = int(read_address(chip,addr),0) & 0xFF
        return result

#Write 8 bit value into internal addr of chip. chip is the actual I2C slave address and addr the internal address of the dev$

def write8(chip, addr, value):
        value = value & 0xFF
        write_address(chip, addr, value)

def write_param(address,p,v):
        write_address(address,0x17,v)
        write_address(address,0x18,p | 0xA0)
        value = read_address(address,0x2E)
        return value

def reset():
        write_address(0x60,0x08,0x00)
        write_address(0x60,0x09,0x00)
        write_address(0x60,0x04,0x00)
        write_address(0x60,0x05,0x00)
        write_address(0x60,0x06,0x00)
        write_address(0x60,0x03,0x00)
        write_address(0x60,0x21,0xFF)
        write_address(0x60,0x18,0x01)
        time.sleep(0.01)
        write_address(0x60,0x07,0x17)
        time.sleep(0.01)

def calibration():
        write_address(0x60,0x13,0x29)
        write_address(0x60,0x14,0x89)
        write_address(0x60,0x15,0x02)
        write_address(0x60,0x16,0x00)
        write_param(0x60,0x01,0x80 | 0x20 | 0x10 | 0x01)
        write_address(0x60,0x03,0x01)
        write_address(0x60,0x04,0x01)
        write_address(0x60,0x0F,0x03)
        write_param(0x60,0x07,0x03)
        write_param(0x60,0x02,0x01)
        write_param(0x60,0x0B,0x00)
        write_param(0x60,0x0A,0x70)
        write_param(0x60,0x0C,0x20 | 0x04)
        write_param(0x60,0x1E,0x00)
        write_param(0x60,0x1D,0x70)
        write_param(0x60,0x1F,0x20)
        write_param(0x60,0x11,0x00)
        write_param(0x60,0x10,0x70)
        write_param(0x60,0x12,0x20)
        write_address(0x60,0x08,0xFF)
        write_address(0x60,0x18,0x0F)


def readU16(address, register, little_endian=True):
        result = read_word_data(address,register) & 0xFFFF
        if not little_endian:
                result = ((result << 8) & 0xFF00) + (result >> 8)
        return result


def readU16LE(address, register):
        return readU16(address,register, little_endian=True)


def read_uv():
        uvrel = float(readU16LE(0x60,0x2C))/100
        als = float(readU16LE(0x60,0x22))
        alsir = float(readU16LE(0x60,0x24))
        vis = (float(als)*5.41)-(float(alsir)*0.08)
        uvabs = float(readU16LE(0x60,0x2C))*float(readU16LE(0x60,0x22))/100000
        print 'SI1145 UV Relative Index : ',uvrel
        print 'SI1145 UV Absolute       : ',uvabs
        print 'SI1145 ALS Vis + IR      : ',als
        print 'SI1145 Visible lux       : ',vis
        print 'SI1145 IR                : ',alsir
        print 'SI1145 Proximity         : ',float(readU16LE(0x60,0x26))
        print 'SI1145 Irr W/m           : ',round(readU16LE(0x60,0x24)*0.0079,2)

reset()
calibration()
read_uv()