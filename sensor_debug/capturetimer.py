import time
from timeloop import Timeloop
from datetime import timedelta

# This code uses the Timedelta library to schedule when readings are captured
# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679

tl = Timeloop()

execfile('humidex_debug.py')
print("Initial humidex capture ",time.time())

@tl.job(interval=timedelta(minutes=10))
def humidex_capture():
	execfile('humidex_debug.py')
	print("Humidex captured ",time.time())

if __name__ == "__main__":
    tl.start(block=True)