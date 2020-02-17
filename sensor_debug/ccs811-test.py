# Adapted from https://gist.github.com/jiemde/481161c426c90c73e52aa51acfd94c2b

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# default address
CCS811_ADDR = 0x5A

# Commands
CCS811_STATUS = 0x00
CCS811_MEAS_MODE = 0x01
CCS811_ALG_RESULT_DATA = 0x02
CCS811_RAW_DATA = 0x03
CCS811_ENV_DATA = 0x05
CCS811_NTC = 0x06
CCS811_THRESHOLDS = 0x10
CCS811_BASELINE = 0x11
CCS811_HW_ID = 0x20
CCS811_HW_VERSION = 0x21
CCS811_FW_BOOT_VERSION = 0x23
CCS811_FW_APP_VERSION = 0x24
CCS811_ERROR_ID = 0xE0
CCS811_APP_START = 0xF4
CCS811_SW_RESET = 0xFF

value = bus.read_i2c_block_data(CCS811_ADDR, CCS811_STATUS, 1)
print (value[0] << 3)

bus.write_i2c_block_data(CCS811_ADDR, CCS811_MEAS_MODE, [0x10])

value = bus.read_i2c_block_data(CCS811_ADDR, CCS811_STATUS, 1)
print (value[0] << 3)
