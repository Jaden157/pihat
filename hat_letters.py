#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("|", (255, 0, 0))
time.sleep(.05)
sense.show_letter("|", (255, 255, 255))
time.sleep(.05)
sense.show_letter("|", (0, 0, 255))
time.sleep(.05)
sense.show_letter("|", (255, 255, 0))
time.sleep(.05)
sense.show_letter("|", (255, 0, 255))
time.sleep(.05)
sense.show_letter("|", (0, 255, 255))
time.sleep(.05)
sense.clear()
