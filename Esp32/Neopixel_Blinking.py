#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic 6: Neopixel blinking with different colours

import machine,neopixel,time

pix=1
led_pin=48

led=neopixel.NeoPixel(machine.Pin(led_pin),pix)
print("Neopixel Led is ON")

while True:
    led[0]=(225,225,225)
    led.write()
    time.sleep(1)
    
    led[0]=(125,25,125)
    led.write()
    time.sleep(1)
    
    