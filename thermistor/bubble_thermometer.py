# This script creates a neopixel theromometer

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import adafruit_thermistor
from math import floor

thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

is_running = True

col_scale = [
    (191, 0, 255),
    (153, 0, 255),
    (123, 0, 255),
    (64, 0, 255),
    (0, 128, 255),
    (191, 255,0),
    (255, 255, 0),
    (255, 191, 0),
    (255, 128, 0),
    (255, 64, 0)]

while is_running:
    pixels.fill((0, 0, 0))
    pixels.show()
    temp_f = thermistor.temperature * 9 / 5 + 32

    try:
        temp_range = floor(temp_f / 10)
        temp_range = 10 if temp_range > 10 else temp_range
        print(temp_f)

        for i in range(temp_range):
            pixels[i] = col_scale[i]
            pixels.show()
            time.sleep(0.25)
    except ZeroDivisionError as e:
        print(e)

    time.sleep(1)
