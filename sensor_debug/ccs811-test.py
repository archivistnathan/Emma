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

# CCS811_REF_RESISTOR = const(100000)

class CCS811(object):

	def __init__(self):
        self.addr = CCS811_ADDR
        self.tVOC = 0
        self.CO2 = 0

    def print_error(self):
        """Error code. """

        error = self.bus.read_i2c_block_data(self.addr, CCS811_ERROR_ID, 1)
        message = 'Error: '

        if (error[0] >> 5) & 1:
            message += 'HeaterSupply '
        elif (error[0] >> 4) & 1:
            message += 'HeaterFault '
        elif (error[0] >> 3) & 1:
            message += 'MaxResistance '
        elif (error[0] >> 2) & 1:
            message += 'MeasModeInvalid '
        elif (error[0] >> 1) & 1:
            message += 'ReadRegInvalid '
        elif (error[0] >> 0) & 1:
            message += 'MsgInvalid '

        print(message)


    def configure_ccs811(self):
        # Check that the HW id is correct
        hardware_id = self.bus.read_i2c_block_data(self.addr, CCS811_HW_ID, 1)
        # print(hardware_id)

        if (hardware_id [0] != 0x81):
            # print ("error!")
            raise ValueError('CCS811 not found. Please check wiring.')

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at Startup.')

        if not self.app_valid():
            raise ValueError('Error: App not valid')

        self.bus.write_byte(self.addr, CCS811_APP_START)

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at AppStart.')

        self.set_drive_mode(1)

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at setDriveMode.')

    def setup(self):

        print('Starting CCS811 Read')
        self.configure_ccs811()

        result = self.get_base_line()

        # print("baseline for this sensor: ")
        if result < 0x100:
            print('0')
        if result < 0x10:
            print('0')
        print('baseline for this sensor =   ', result)

    def get_base_line(self):

        b = self.bus.read_i2c_block_data(self.addr, CCS811_BASELINE, 2)
        baselineMSB = b[0]
        baselineLSB = b[1]
        baseline = (baselineMSB << 8) | baselineLSB
        return baseline

    def check_for_error(self):
        value = self.bus.read_i2c_block_data(self.addr, CCS811_STATUS, 1)
        # print('Value_error', value)
        # print(value[0] )

        v = ((value[0] >> 0) & 1)
        # print('V error = ', v)
        return ((value[0] >> 0) & 1)

    def app_valid(self):
        value = self.bus.read_i2c_block_data(self.addr, CCS811_STATUS, 1)
        # print('Value', value)
        # print(value[0])

        v = ((value[0] >> 4) & 1)
        # print('V valid = ', v)
        return ((value[0] >> 4) & 1)

    def set_drive_mode(self, mode):
        if mode > 4:
            mode = 4

            #   Clean_reg

        self.bus.write_i2c_block_data(self.addr, CCS811_MEAS_MODE, 0x00)
        time.sleep(1)

        setting = self.bus.read_byte_data(self.addr, CCS811_MEAS_MODE)
        # print('Setting_start =  ', setting, setting[0])

        buf1 = setting[0] & (~(0b00000111 << 4))
        buf2 = buf1 | (mode << 4)

        self.bus.write_i2c_block_data(self.addr, CCS811_MEAS_MODE, bytes([buf2]))
        # i2c.writeto_mem(device, CCS811_MEAS_MODE, 0x10)


    def data_available(self):

        value = self.bus.read_i2c_block_data(self.addr, CCS811_STATUS, 1)
        return value[0] << 3


    def readeCO2(self):
        """ Equivalent Carbone Dioxide in parts per millions. Clipped to 400 to 8192ppm."""

        self.setup()

        if self.data_available():

            d = self.bus.read_i2c_block_data(self.addr, CCS811_ALG_RESULT_DATA, 4)

            co2MSB = d[0]
            co2LSB = d[1]

            return ((co2MSB << 8) | co2LSB)

        elif self.check_for_error():
                self.print_error()


    def readtVOC(self):
        """ Total Volatile Organic Compound in parts per billion. """

        self.setup()

        if self.data_available():

            d = self.bus.read_i2c_block_data(self.addr, CCS811_ALG_RESULT_DATA, 4)

            tvocMSB = d[2]
            tvocLSB = d[3]

            return ((tvocMSB << 8) | tvocLSB)

        elif self.check_for_error():
                self.print_error()

    def reset(self):
        """ Initiate a software reset. """

        seq = bytearray([0x11, 0xE5, 0x72, 0x8A])
        self.bus.write_i2c_block_data(self.addr, CCS811_SW_RESET, seq)

ccs811.configure_ccs811()
ccs811.setup()

    # def set_environmental_data(self, hum, temp):
    #     """ use of temperature and humidity when computing eCO2 and TVOC values """
    #     # Humidity in %
    #     # T° in Celsius
    #     hum = int(humidity) << 1
    #     temp = 30.5
    #     buf = byterray([hum_perc, temp])
    #     self.bus.write_i2c_block_data(self.addr, CCS811_ENV_DATA, buf)