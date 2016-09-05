from rrb2 import *
import time

rr = RRB2()

def fw(speed=1):
	rr.set_motors(speed, 0, speed, 0)

def bk(speed=1):
	rr.set_motors(speed, 1, speed, 1)


def right(angle, speed=1):
	rr.set_motors(speed, 1, speed * (1-angle), 1)

def left(angle, speed=1):
	rr.set_motors(speed * (1-angle), 1, speed, 1)



for n in range(5):
	fw(0.2 * n)
	time.sleep(1)

bk()

time.sleep(2)

fw()

time.sleep(3)

right(0.7)

time.sleep(3)

right(1)

time.sleep(1)

