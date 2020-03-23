# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Main code for running sensors
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# import configuration file and required libraries
import config
import time
from timeloop import Timeloop
from datetime import timedelta

# This code uses the Timedelta library to schedule when readings are captured
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679

tl = Timeloop()

# initial sensor data capture

execfile('capture_humidex.py')
print("Humidex capture started")

execfile('capture_illuminance.py')
print("Illuminance capture started")

execfile('capture_acceleration.py')
print("Acceleration capture started")

execfile('capture_soundlevel.py')
print("Sound level capture started")

# start thread outside of the timeloop for GPIO state based user count
import capture_usercount

# time sensor data capture via timeloop

# Humidex and Illuminance, minimum frequency 1 second
@tl.job(interval=timedelta(minutes=10))
def humidex_illuminance_capture():
	execfile('capture_humidex.py')
	print("Humidex captured ")
	
	execfile('capture_illuminance.py')
	print("Illuminance captured")

# Acceleration, minimum frequency 1 second
@tl.job(interval=timedelta(seconds=10))
def acceleration_capture():
	execfile('capture_acceleration.py')
	print("Acceleration captured")

# Sound level, minimum frequency 10 seconds
@tl.job(interval=timedelta(seconds=10))
def soundlevel_capture():
	execfile('capture_soundlevel.py')
	print("Sound level captured ")

if __name__ == "__main__":
    tl.start(block=True)