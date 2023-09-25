#Author Name: Yash Rajput
#micropython script for esp32s3
#Project Title: Making a webserver for remotely accessing various output sensors(in this case NeoPixel led)


import machine
import network
import time
import sys
import gc
try:
    import usocket as socket
except:
    import socket
from neopixel import NeoPixel

# Run garbage collector
gc.collect()

# Configure Neopixel
pix = 1
led_pin = machine.Pin(12, machine.Pin.OUT)
np = NeoPixel(led_pin, pix)

HOST = '192.168.112.239'
PORT = 80
BUFFER = 1024
FORMAT = 'utf-8'

timeout = 0 
wlan = network.WLAN(network.STA_IF)
wlan.active(False)
time.sleep(0.5)
wlan.active(True)
wlan.connect('Exp','81234567')
if not wlan.isconnected():
    print('Connecting to network..')
    while not wlan.isconnected() and timeout < 10:
        print(10-timeout)
        timeout += 1
        time.sleep(1)
    if wlan.isconnected():
        print('network config: ',wlan.ifconfig())
    else:
        print('could not connect')
        sys.exit()

def web_page():
    if isLedBlinking == True:
        led_state = 'Blinking'
        print('LED is Blinking')
    else:
        if np[0] == (0, 125, 125):
            led_state = 'ON (Cyan)'
            print('LED is ON (Cyan)')
        elif np[0] ==(0,0,0):
            led_state = 'OFF'
            print('LED is OFF')

    html_page = """    
    <html>    
    <head>    
     <meta content="width=device-width, initial-scale=1" name="viewport"></meta>    
    </head>    
    <body>    
     <center><h2>ESP32 Web Server in MicroPython </h2></center>    
     <center>    
      <form>    
      <button name="LED" type="submit" value="CYAN"> LED ON (Cyan) </button>  
      <button name="LED" type="submit" value="OFF"> LED OFF </button>
      <button name="LED" type="submit" value="BLINK"> LED BLINK </button>  
      </form>    
     </center>    
     <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>    
    </body>    
    </html>"""  
    return html_page   

timer0 = machine.Timer(0)
def handle_callback(timer):
    global isLedBlinking
    np[0] = (0, 0, 0) if np[0] == (0, 125, 125) else (0, 125, 125)
    np.write()

isLedBlinking = False

# create server socket at esp32
# if socket is not created, script terminated
try:
    # create socket (TCP)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # bind the socket with IP and PORT
    # blank IP specifies that socket is reachable by any addr
    # the machine happens to have
    # web server port is 80
    s.bind(('',80))
    # start listening for clients 
    s.listen(5)
    print('Socket created')
except Exception as e:
    print('Error>>',str(e))
    sys.exit()

while True:
    # accept client connection 
    conn,addr = s.accept()
    print('client connected from ',addr)
    # recieve data from client machine
    request = conn.recv(1024)
    request = str(request)
    print('request content = ',request)
    # find the request 
    led_on = request.find('/?LED=CYAN')
    led_off = request.find('/?LED=OFF')
    led_blink = request.find('/?LED=BLINK')
    
    if led_on == 6:
        np[0] = (0, 125, 125)
        np.write()
        print('LED ON (Cyan)')
    elif led_off == 6:
        # turn off the LED
        np[0] = (0, 0, 0)
        np.write()
        print('LED OFF')
        if isLedBlinking == True:
            timer0.deinit()
            isLedBlinking = False
    elif led_blink == 6:
        # blink the LED
        print('LED is Blinking')
        isLedBlinking = True
        timer0.init(period=500, mode=machine.Timer.PERIODIC, callback=handle_callback)
    # send response back to client machine 
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    # close the connection
    conn.close()