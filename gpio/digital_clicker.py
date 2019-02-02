# Tapping a button will send a signal to another device via IO connectors

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel


btn_a = DigitalInOut(board.BUTTON_A)
btn_a.direction = Direction.INPUT
btn_a.pull = Pull.DOWN

a1 = DigitalInOut(board.A1)
a1.direction = Direction.OUTPUT

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)

is_running = True

while is_running:
    try:
        a1.value = False
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.09)
        if btn_a.value:
            a1.value = True
            pixels.fill((255, 255, 255))
            pixels.show()
    except Exception as e:
        print(e)

    time.sleep(0.01)