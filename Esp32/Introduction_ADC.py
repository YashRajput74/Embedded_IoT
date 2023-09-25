#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic_8: Introduction to ADC

from machine import Pin,ADC #since I am only using Pin and ADC from machine module I imported that only
from time import sleep

sensor=ADC(Pin(4))
sensor.atten(ADC.ATTN_11DB)
sensor.width(ADC.WIDTH_9BIT)

while True:
    sensor_value=sensor.read()
    print(sensor_value)
    sleep(0.1)