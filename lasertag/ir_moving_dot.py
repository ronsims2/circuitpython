########################################################################################
# This program should cycle around the neo pixels when you push the channel+ button.
# Mari noticed that the channel- button doesn't advance the lights. It falls into the
# error block.
#
#
#
#
#
#
########################################################################################

import time
import board
import pulseio
import adafruit_irremote
import neopixel

is_running = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()
counter = 0

while is_running:
    try:
        pulses = decoder.read_pulses(pulsein)

        if counter > 0 and counter % 10 == 0:
            counter = 0

        if pulses is not None:
            pixels[counter] = (20, 230, 80)
            pixels.show()
            time.sleep(0.05)
            pixels[counter] = (0, 0, 0)
            pixels.show()
            print(counter)
            #print(pulses)
            received_code = decoder.decode_bits(pulses, debug=False)
            pulses = None
            counter += 1



        if received_code is not None:
            pass
            # print(received_code)

    except Exception as e:
        time.sleep(0.05)
        pixels[counter] = (0, 0, 0)
        pixels.show()
        pulses = None
        print(e)


    time.sleep(0.125)