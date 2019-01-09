#!/usr/bin/env python

import time
from sys import exit

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

import blinkt

blinkt.set_clear_on_exit()

def show_graph(v):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if x > v:
                blinkt.set_pixel(x, 0, 0, 0)
        elif x < blinkt.NUM_PIXELS/3.0:
		blinkt.set_pixel(x, 0, 50, 0)
	elif x < blinkt.NUM_PIXELS*2.0/3.0:
		blinkt.set_pixel(x, 50, 25, 0)
	elif x < blinkt.NUM_PIXELS*3.0/3.0:
		blinkt.set_pixel(x, 50, 0, 0)
    blinkt.show()

blinkt.set_brightness(0.04)

while True:
    load = psutil.cpu_percent() / 100.0
    show_graph(load)
    time.sleep(0.2)
