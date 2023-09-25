#Author Name: Yash Rajput
#micropython script for esp32s3
#Project Title: Making a server for remotely accessing various output sensors(in this case NeoPixel led)

import socket
import sys
import threading

#server credentials
IP=socket.gethostbyname(socket.gethostname())
PORT=54321

#global variables
BUFFER=1024
FORMAT='utf-8'
client_list=[]

try:
    sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sckt.bind((IP,PORT))
    sckt.listen()
    print(f"Server is listening from clients at {IP}:{PORT}")
except socket.error as e:
    print(f"Error in creating socket:{e}")
    sys.exit()

def broadcast(msg):
    print(f"{msg}")
    for c in client_list:
        c.send(msg.encode(FORMAT))
        if not msg:
            print("No msg from esp")
            break

def client_handle(conn,):
    while True:
        try:
            print("Write either YELLOW or PURPLE or CYAN or RED or GREEN or BLUE or WHITE")
            msg=input(">> ")
            broadcast(msg)
        except:
            index=client_list.index(conn)
            client_list.remove(conn)
            broadcast(f"{conn} has left the chat")
            break

while True:
    try:
        conn,addr=sckt.accept()
        print(f"{addr} connected with server")
        client_list.append(conn)
        broadcast(f"{conn} has joined the chat")
        client_thread=threading.Thread(target=client_handle,args=(conn,))
        client_thread.start()
        active_connections=threading.active_count()-1
    except Exception as e:
        print(f"error in creating thread {e}")
        break
    except KeyboardInterrupt:
        print("Server is closed")
        break