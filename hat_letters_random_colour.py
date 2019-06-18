#!/usr/bin/env python

from sense_hat import SenseHat
import time 
import random
sense = SenseHat()
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

sense.show_letter("H", (r, g, b))
time.sleep(1)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("i", (r, g, b))
time.sleep(1)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("!", (r, g, b))
time.sleep(1)

sense.clear()
