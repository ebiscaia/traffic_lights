# Implementing the logic for the traffic lights
# 1 = north
# 2 = east
# 3 = south
# 4 = west

# Lights 2 and 4 will be on if keys 2 and 4 are on
# Lights 2 and 4 will be on if either key 2 or 4 are on
# and keys 1 and 3 are not both on
# Lights 2 and 4 will be on if neighter keys 1 and 3 are on

from machine import Pin


def ledOff(lights):
    for light in lights:
        light.off()


def ledOn(lights):
    for light in lights:
        light.on()


def keySum(keys):
    sum = 0
    for key in keys:
        sum += key.value()
    return sum


led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(3, Pin.OUT)
key1 = Pin(16, Pin.IN)
key2 = Pin(17, Pin.IN)
key3 = Pin(18, Pin.IN)
key4 = Pin(19, Pin.IN)


# Aggregate the leds and keys into lists corresponding to their directions
NS_leds = [led1, led3]
EW_leds = [led2, led4]
NS_keys = [key1, key3]
EW_keys = [key2, key4]

leds = [led1, led2, led3, led4]


# Loop through the keys and the corresponding leds on/off accordingly
while True:
    ledOff(leds)

    NS_sum = keySum(NS_keys)
    EW_sum = keySum(EW_keys)
    if EW_sum >= NS_sum:
        ledOn(EW_leds)
    else:
        ledOn(NS_leds)
