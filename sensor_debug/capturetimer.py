import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

execfile('humidex.py')
print("Initial humidex capture ",time,time())

@tl.job(interval=timedelta(seconds=30))
def humidex_capture():
	execfile('humidex_debug.py')
	print("Humidex captured ",time,time())

if __name__ == "__main__":
    tl.start(block=True)