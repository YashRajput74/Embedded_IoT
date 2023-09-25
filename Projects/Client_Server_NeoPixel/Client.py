#Author Name: Yash Rajput
#micropython script for esp32s3
#Project Title: Making a client for remotely accessing various output sensors(in this case NeoPixel led)

import socket, sys, machine, neopixel, network, time

pix = 1
led = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(led, pix)

HOST = '192.168.112.239' #type your server's IP Address
PORT = 54321
BUFFER = 1024
FORMAT = 'utf-8'

def connect_wifi(ssid, psk, timeout):
    wifi = network.WLAN(network.STA_IF)
    wifi.active(False)
    time.sleep(1)
    wifi.active(True)
    t = 0
    wifi.connect(ssid, psk)
    if not wifi.isconnected():
        print("not able to connect")
        while (not wifi.isconnected() and t < timeout):
            print(timeout - t)
            t += 1
            time.sleep(1)
    if wifi.isconnected():
        print("connection established")
    else:
        print("Unable to connect")
    return wifi

def set_led_color(color):
    if color == "YELLOW":
        np.fill((125, 125, 0))
    elif color == "PURPLE":
        np.fill((125, 0, 125))
    elif color == "CYAN":
        np.fill((0, 125, 125))
    elif color == "RED":
        np.fill((125,0, 0))
    elif color == "GREEN":
        np.fill((0, 125, 0))
    elif color == "BLUE":
        np.fill((0, 0, 125))
    elif color == "WHITE":
        np.fill((125, 125, 125))
    else:
        np.fill((0, 0, 0))
    np.write()

try:
    wifi = connect_wifi("Exp", '81234567', 10)
    print("IP of my esp device is: ")
    print(wifi.ifconfig())
    if wifi.isconnected():
        try:
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.connect((HOST, PORT))
            print("Connection Established")
            print(f"Server is up at: {HOST}:{PORT}")
        except Exception as e:
            print(f"Error in socket creation {e}")
            sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            sys.exit()
    else:
        print("check connection")
except KeyboardInterrupt:
    print("EXIT")
except Exception as e:
    print(e)

def cmnd(sckt):
    while True:
        try:
            msg = sckt.recv(BUFFER).decode(FORMAT)
            if not msg:
                print("No msg from server")
            else:
                print(f"Received message from server: {msg}")
                set_led_color(msg)
                new_msg = f"We have turned LED {msg}"
                sckt.send(new_msg.encode(FORMAT))
        except Exception as e:
            print(f"Error is handling client {e}")
            sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            sys.exit()

if __name__ == "__main__":
    cmnd(sckt)