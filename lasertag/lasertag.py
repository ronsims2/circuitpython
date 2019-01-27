from adafruit_circuitplayground.express import cpx

is_running = True

while is_running:
    if cpx.button_a:
        print("Temperature:", cpx.temperature)
    cpx.red_led = cpx.button_b
