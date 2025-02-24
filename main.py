# Add a group of switches and if it is on a corresponding led will
# turn on. Otherwise the led will be off

from machine import Pin

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(3, Pin.OUT)
key1 = Pin(16, Pin.IN)
key2 = Pin(17, Pin.IN)
key3 = Pin(18, Pin.IN)
key4 = Pin(19, Pin.IN)


# Aggregate the leds and keys into lists
leds = [led1, led2, led3, led4]
keys = [key1, key2, key3, key4]

# Loop through the keys and the corresponding leds on/off accordingly
while True:
    for index, key in enumerate(keys):
        if key.value():
            leds[index].on()
        else:
            leds[index].off()
