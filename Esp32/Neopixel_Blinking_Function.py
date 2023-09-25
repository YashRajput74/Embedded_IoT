#Author Name: Yash Rajput
#micropyhon script for esp32s3
#Topic_7: Neopixel Blinking using Function

from machine import Pin
from newopixel import NeoPixel
import time

np=NeoPixel(Pin(48),1)

start_time_red=time.ticks_ms()
start_time_green=time.tick_ms()
blink_interval_red=1000
blink_interval_green=1500

def blink_red():
    global start_time_red,blink_interval_red,red
    if(time.ticks_ms()-start_time_red)>=blink_interval_red:
        start_time_red=time.ticks_ms()
        if green==255:
            green=0
        elif red==0:
            red=255
        np[0]=(red,0,0)
        np.write()
        print("Led RED is ON" if red==255 else "Led RED is OFF")