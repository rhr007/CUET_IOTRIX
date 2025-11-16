from machine import ADC, Pin
from time import sleep

ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)

while True:

    ldr_value = ldr.read()

    print("LDR Value:", ldr_value)

    sleep(1)