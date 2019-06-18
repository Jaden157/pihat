#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

X = (200, 255, 110)
Y = (0, 0, 255)

speed = 0.05

message = "Hello World"
sense.show_message(message, speed, text_colour=X, back_colour=Y)

sense.clear()
