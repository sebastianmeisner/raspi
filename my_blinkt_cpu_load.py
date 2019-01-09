#!/usr/bin/env python

import time
from sys import exit
import math

def floatRgb(mag, cmin, cmax):
    """ Return a tuple of floats between 0 and 1 for R, G, and B. """
    # Normalize to 0-1
    try: x = float(mag-cmin)/(cmax-cmin)
    except ZeroDivisionError: x = 0.5 # cmax == cmin
    blue  = min((max((4*(0.75-x), 0.)), 1.))
    red   = min((max((4*(x-0.25), 0.)), 1.))
    green = min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return red, green, blue


def rgb(mag, cmin, cmax):
    """ Return a tuple of integers, as used in AWT/Java plots. """
    red, green, blue = floatRgb(mag, cmin, cmax)
    return int(red*255), int(green*255), int(blue*255)

def strRgb(mag, cmin, cmax):
    """ Return a hex string, as used in Tk plots. """
    return "#%02x%02x%02x" % rgb(mag, cmin, cmax)

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
