#Author Name: Yash Rajput
#micropython Script for esp32s3
#Topic_11:USing esp32s3 as a station point

import network,time,urequests

def connect_wifi(ssid,psk,timeout):
    wifi=network.WLAN(network.STA_IF)
    wifi.active(False)
    time.sleep(1)
    wifi.active(True)
    t=0
    wifi.connect(ssid,psk)
    if not wifi.isconnected():
        print("Trying to connect to network...")
        while(not wifi.isconnected() and t<timeout):
            print(timeout-t)
            t+=1
            time.sleep(1)
        if wifi.isconnected():
            print("Connected to network")
        else:
            print("Unable to connect")
        return wifi
# I made a function which will try to connect to wifi with given ssid and password.

try:
    wifi=connect_wifi("Exp",'81234567',10)
    print("Ip of my esp device:")
    print(wifi.ifconfig())
    if wifi.isconnected():
        request34=urequests.get('https://example.com')
        print("request succesful" if request34.status_code is 200 else "request unss")
    else:
        print("check connection")
except KeyboardInterrupt:
    print("Exit")
except Exception as e:
    print(e)