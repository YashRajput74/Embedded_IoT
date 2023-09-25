#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic_3: Introduction to Button

import machine
import time

led=machine.Pin(1,machine.Pin.OUT)
button=machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)

while True:
    if button.value()==0:
        led.value(not led.value())
        print("Led is ON" if led.value() else "Led is OFF")
        while button.value()==0:
            time.sleep(0.01) # this approach is childish but it works for avoiding debouncing of a button
            #pass #if you do not want to use delay then vut above line and write pass