# Code adapted from https://tutorials-raspberrypi.com/configure-and-read-out-the-raspberry-pi-gas-sensor-mq-x

# Set-up SPI communication

from configure_gaslevel import *
import time, datetime
import threading

# Calibrate sensor and determine Ro
mq = MQ();

# Thread control
readgas = 1

# Read data
def readgaslevel():
	while (global readgas == 1):
		perc = mq.MQPercentage()
		print("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
		time.sleep(0.1)

print "Gas level monitoring started"

try:
	thread = threading.Thread(target=readgaslevel)
	thread.start()
except KeyboardInterrupt:
	readgas == 0
	print "Gas level monitoring stopped"