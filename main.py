# Turn the internal LED on to check if the board
# is functional and MicroPython was installed
# correctly

from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
