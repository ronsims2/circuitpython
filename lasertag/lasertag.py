import time
import board
import pulseio
import adafruit_irremote
import neopixel

is_running = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

while is_running:
    pixels.fill((0, 0, 0))
    pulses = decoder.read_pulses(pulsein)

    if pulses is not None:
        pixels.fill((20, 230, 80))
        print(pulses)

    try:
        received_code = decoder.decode_bits(pulses, debug=False)
        if received_code is not None:
            print(received_code)

    except Exception as e:
        print(e)


    time.sleep(0.125)