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

execfile('capture_humidex.py')
print("Humidex capture started",time.time())

execfile('capture_illuminance.py')
print("Illuminance capture started",time.time())

@tl.job(interval=timedelta(seconds=10))
def humidex_capture():
	execfile('capture_humidex.py')
	print("Humidex captured ",time.time())
	
	execfile('capture_illuminance.py')
	print("Illuminance captured",time.time())

if __name__ == "__main__":
    tl.start(block=True)