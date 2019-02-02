# This script uses a button to turn on neopixels and dims them.

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

btn_a = DigitalInOut(board.BUTTON_A)
btn_a.direction = Direction.INPUT
btn_a.pull = Pull.DOWN

btn_b = DigitalInOut(board.BUTTON_B)
btn_b.direction = Direction.INPUT
btn_b.pull = Pull.DOWN

is_running = True

while is_running:
    if btn_a.value:
        pixels.fill((42, 88, 134))
        pixels.show()
    else:
        pixels.fill((0, 0,0))
        pixels.show()

    if btn_b.value:
        if pixels.brightness > 0:
            pixels.brightness -= 0.02
        else:
            pixels.brightness = 1

    time.sleep(0.01)