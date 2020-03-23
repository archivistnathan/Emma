# Code adapted from https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x

# Set-up SPI communication

from configure_gaslevel import *
import time, datetime

mq = MQ();
perc = mq.MQPercentage()
print("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))