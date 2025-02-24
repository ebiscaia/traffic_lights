# Add a switch and if it is on the external led will
# blink. Otherwise the led will be off

from machine import Pin
import time

led = Pin(0, Pin.OUT)
key = Pin(16, Pin.IN)

while True:
    if key.value():
        led.toggle()
        time.sleep(1)
    else:
        led.off()
