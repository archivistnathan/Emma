import time
from timeloop import Timeloop
from datetime import timedelta

t1 = Timeloop()

@tl.job(interval=timedelta(seconds=30))
def humidex_capture():
	execfile(humidex.py)
	print("Humidex captured ",time,time())

if __name__ == "__main__":
    tl.start(block=True)