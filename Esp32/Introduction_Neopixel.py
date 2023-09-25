#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic 5: Introduction to Neopixel

#esp32s3 provides a Neopixel Led on Board

import neopixel
import machine
import time

pix=1 #since I have only 1 led this value is 1 if it were a strip the value will increase
led_pin=48
led=neopixel.NeoPixel(machine.Pin(led_pin),pix)
print("Neopixel Led")
           
while True:
    led[0]=(25,125,125)
    led.write()
    time.sleep(1)