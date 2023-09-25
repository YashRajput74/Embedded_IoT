#Author Name: Yash Rajput
#micropython Script for esp32s3
#Topic_10:Creating a access point using esp32s3

import network

wifi=network.WLAN(network.AP_IF)
wifi.active(True)

try:
    wifi.config(essid="Dev_network",password='12345678',authmode=network.AUTH_WPA_WPA2_PSK)
    print(wifi.ifconfig())
except KeyboardInterrupt:
    print("Exit")