# Turn an external LED on to check if the board
# is functional and MicroPython was installed
# correctly

from machine import Pin
import time

led = Pin(0, Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
