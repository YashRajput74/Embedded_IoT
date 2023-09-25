#Author Name: Yash Rajput
#micropython script for esp32s3
#Topic_4: Button press Event

#defining Pins
led_pin=1
button_pin=0
#instead of writinng these numbers within the code I wrote it here so I can now change it anytime without disturbing the code
led=machine.Pin(led_pin,machine.Pin.OUT)
button=machine.Pin(button_pin,machine.Pin.IN,machine.pin.PULL_UP)

def button_isr(pin): #isr here is representing Interrupt service routine
    led.value(not led.value())
    print("Led is ON" if led.value() else "Led is OFF")
    
button.irq(trigger=machine.Pin.IRQ_FALLING.handler=button_isr) #irq here is representing Interrupt Request

try:
    while True:
        pass   # with this our functio will run continuosly
except KeyboardInterrupt:
    print("Exit the program using Keyboard)