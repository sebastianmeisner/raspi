#!/usr/bin/env python

##########################################################
## Show your current CPU usage on your PiGlow!          ##
##                                                      ##
## Requires psutil - sudo apt-get install python-psutil ##
##                                                      ##
## Example by Jason - @Boeeerb                          ##
##########################################################

import piglow
from time import sleep
import psutil

def leg_bar_intensity(leg_index, percentage, intensity=1.0):
    """Display a bargraph on a leg.
    A leg/arm/spoke is the line of 6 LEDs the emanates from the center of Piglow to the edge.
    :param leg_index: leg from 0 to 2
    :param percentage: percentage to display in decimal
    :param intensity:  percentage of maximum intensity
    """

    # From inner led to outer led
    legs = [
        [5,4,3,2,1,0],
        [11,10,9,8,7,6],
        [17,16,15,14,13,12]
    ]
    if percentage > 1.0 or percentage < 0:
        raise ValueError("percentage must be between 0.0 and 1.0")

    if intensity > 1.0 or intensity < 0:  
        raise ValueError("intensity must be between 0.0 and 1.0")

    # 1530 = 6 * 255
    amount = int(1530.0 * percentage * intensity)
    for led_index in legs[leg_index % 3]:
        piglow.set(led_index, int(255*intensity) if amount > 255*intensity else int(amount*intensity) )
        amount = 0 if amount < (255*intensity) else amount - (255*intensity)


value=0
arm = 0
while True:

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()[2]
    piglow.all(0)
    leg_bar_intensity(0, cpu*0.01, 0.25)
    leg_bar_intensity(1, mem*0.01, 0.25)

#    value +=0.1
#    if value > 1.0:
#        value = 0
#        arm += 1

#    piglow.leg_bar(0, cpu/100.0)
#    if cpu < 5:
#        piglow.red(20)
#    elif cpu < 20:
#        piglow.red(20)
#        piglow.orange(20)
#    elif cpu < 40:
#        piglow.red(20)
#        piglow.orange(20)
#        piglow.yellow(20)
#    elif cpu < 60:
#        piglow.red(20)
#        piglow.orange(20)
#        piglow.yellow(20)
#        piglow.green(20)
#    elif cpu < 80:
#        piglow.red(20)
#        piglow.orange(20)
#        piglow.yellow(20)
#        piglow.green(20)
#        piglow.blue(20)
#    else:
#        piglow.all(20)
    piglow.show()
    sleep(0.2)
