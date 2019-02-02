# This script creates a temp alarm

import time
import board
import neopixel
import adafruit_thermistor
import audioio
import digitalio

thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

is_running = True



while is_running:
    pixels.fill((0, 0, 0))
    pixels.show()
    temp_f = thermistor.temperature * 9 / 5 + 32
    print(temp_f)

    if temp_f < 90:
        wfile = open('./Coin.wav', 'rb')
        for i in range(10):
            pixels[i] = (255, 255, 255)
            pixels.show()
            time.sleep(0.01)
        with audioio.WaveFile(wfile) as wf:
            with audioio.AudioOut(board.A0) as audio:
                audio.play(wf)
                while audio.playing:
                    pass

    time.sleep(0.5)



    time.sleep(1)