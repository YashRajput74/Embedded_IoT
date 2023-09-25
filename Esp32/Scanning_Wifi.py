#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic_9: Scanning nearby Wifi using esp32s3

import network

wifi=network.WLAN(network.STA_IF)
wifi.active(True)
try:
    network=wifi.scan()
    print(network)
#It is to bear in mind that in rare occasion that esp is unable to find aany network it will simply continue scanning till it finds atleast one.
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("EXIT") # I added this so that I can exit from scanning loop anytime at my wish