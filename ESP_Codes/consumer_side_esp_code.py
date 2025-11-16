from machine import ADC, Pin, I2C
from uslib import HCSR04
from time import sleep, time
import urequests 
import oledlib

# OLED init
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = oledlib.SSD1306_I2C(128, 64, i2c)

ride_request_id = None
server_ip = '192.168.1.106'

# --- Sensors ---
ultrasonic = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)


#leds
w_led = Pin(25, Pin.OUT)
y_led = Pin(26, Pin.OUT)
r_led = Pin(27, Pin.OUT)
g_led = Pin(14, Pin.OUT)

buzzer = Pin(12, Pin.OUT)

# LED States
IDLE = 0
REQUEST_SENT = 1
REQUEST_REJECTED = 2
REQUEST_ACCEPTED = 3

def oled_show(text):
    oled.fill(0)           # clear screen
    oled.text(text, 5, 25)
    oled.show()



def set_led(state):
    if state == IDLE:
        w_led.value(1); y_led.value(0); r_led.value(0); g_led.value(0)
        oled_show("IDLE")

    elif state == REQUEST_SENT:
        w_led.value(0); y_led.value(1); r_led.value(0); g_led.value(0)
        oled_show("REQUEST SENT")

    elif state == REQUEST_REJECTED:
        w_led.value(0); y_led.value(0); r_led.value(1); g_led.value(0)
        oled_show("REJECTED")

    elif state == REQUEST_ACCEPTED:
        w_led.value(0); y_led.value(0); r_led.value(0); g_led.value(1)
        oled_show("ACCEPTED")


# --- Buttons ---
btn1_P = Pin(23, Pin.IN, Pin.PULL_DOWN)
btn2_N = Pin(4, Pin.IN, Pin.PULL_DOWN)
btn3_R = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Interrupt flags
btn1_flag = False
btn2_flag = False
btn3_flag = False

def btn1_handler(pin):
    global btn1_flag
    btn1_flag = True

def btn2_handler(pin):
    global btn2_flag
    btn2_flag = True

def btn3_handler(pin):
    global btn3_flag
    btn3_flag = True
    
    
def do_connect():
    import network
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('NMARS', '2122232425')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))

# Attach interrupts
btn1_P.irq(trigger=Pin.IRQ_RISING, handler=btn1_handler)
btn2_N.irq(trigger=Pin.IRQ_RISING, handler=btn2_handler)
btn3_R.irq(trigger=Pin.IRQ_RISING, handler=btn3_handler)


# --- System variables ---
distance_timer_start = None
required_time_usonic = 3
ultrasonic_verified = False
request_sent = False
system_verified = False


def send_request(destination):
    global ride_request_id

    try:
        url = f"http://{server_ip}:8000/request/create?destination={destination}"
        print("Sending request to:", url)

        response = urequests.get(url)

        if response.status_code == 200:
            data = response.json()
            ride_request_id = data.get("request_id")
            print("Ride Request ID stored:", ride_request_id)
            set_led(REQUEST_SENT)
        else:
            print("Server responded with error:", response.status_code)

        response.close()

    except Exception as e:
        print("Error sending request:", e)


def check_status(ride_request_id):
    response = urequests.get(f"http://{server_ip}:8000/request/check?id={ride_request_id}")
    if response.status_code == 200:
        data = response.json()
        
        if data == 'rejected':
            set_led(REQUEST_REJECTED)
        elif data == 'accepted':
            set_led(REQUEST_ACCEPTED)
            buzzer.value(1)
            sleep(1)
            buzzer.value(0)
            
        elif data == 'completed':
            set_led(IDLE)
            ride_request_id = None

    else:
        print("Server responded with error:", response.status_code)

    
    
    

do_connect()
request_sent = False
while True:
    if not request_sent:
        set_led(IDLE)
    
    # ULTRASONIC VERIFICATION
    distance = ultrasonic.distance_cm()
    current_time = time()

    if 10.0 <= distance <= 20.0:
        if distance_timer_start is None:
            distance_timer_start = current_time
        else:
            if current_time - distance_timer_start >= required_time_usonic:
                ultrasonic_verified = True
                print("\n*** 3 Seconds passed --> Ultrasonic Verified ***")
            else:
                ultrasonic_verified = False
                print("\n*** Ultrasonic Not Verified ***")
    else:
        distance_timer_start = None
        ultrasonic_verified = False
        print("\n*** Ultrasonic Not Verified ***")

    # LDR VERIFICATION
    ldr_value = ldr.read()
    ldr_verified = (ldr_value <= 1000)

    # Combined verification
    system_verified = ultrasonic_verified and ldr_verified

    # BUTTON CONTROL USING INTERRUPTS
    if system_verified:

        if btn1_flag:
            print("Destination PAHARTALI selected")
            request_sent = True
            btn1_flag = False
            send_request("PAHARTALI")
            

        elif btn2_flag:
            print("Destination NOAPARA selected")
            request_sent = True
            btn2_flag = False
            send_request("NOAPARA")

        elif btn3_flag:
            print("Destination RAOJAN selected")
            request_sent = True
            btn3_flag = False
            send_request("RAOJAN")
            
        else:
            print("\n*** Both Ultrasonic and LDR Verified but No Button Preesed ***")
            
    else:
        print("\n*** LDR Not Verified ***")


    print("Distance:", distance)
    print("LDR:", ldr_value)
    
    if ride_request_id is not None:
        check_status(ride_request_id)


    sleep(1)

