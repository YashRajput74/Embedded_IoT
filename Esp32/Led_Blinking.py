#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic_2: Blink the led

import machine
import time

led=machine.Pin(1,machine.Pin.OUT) # made a variable for led
print("Variable made for led")
while True:
    led.value(not led.value())
    print("Led is ON" if led.value() else"Led is OFF")
    time.sleep_ms(1000) # I used ms for no particular reason i just wanted to see how it works
    # ms here stands for microseconds it is used to enter the time delay in microseconds