from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED, OutputDevice
import os
import time
import random

from dotenv import load_dotenv
load_dotenv()

if os.getenv('ENVIRONMENT') == "DEV":
    Device.pin_factory = MockFactory()

'''
process:
- check soil moisture once a day? 
-- water:
    - turn on led to signal pump is active, flash 
    - check water level: if full no warning (green LED), if mid send no warning (orange LED),  if low send fill me warning (yello LED), if empty don't run (RED LED)
    - water plants for 10 secs
    - wait 1 min check soil mosture, 
    - if moisture is correct then keep pump off 
    - else restart loop stop after 1hr (Default)
 
 
 not water
- turn on relay switch
- 

'''

def turn_on_relay(soil_moisture):
    # soil need to be above 88% to not be watered
    # relay led and relay GPIO setup

    relay = OutputDevice(24, False, False)
    relay_led = LED(21)

    # turn on light and then blink light to show its watering

    if soil_moisture >= 80:
        print("plants don't need to be watered")

    else:
        print("turning on relay")

        while soil_moisture <= 80:
            relay_led.on()
            time.sleep(0.5)
            relay_led.blink()
            relay.on()
            soil_moisture += 10.0

        print("turning off relay plants are done watered")
        relay_led.off()
        relay.off()



    #!!! IMPORTANT MOCKFACTORY() MOCKS THE FUNCITONS / ATTRIBUTES ASSOCATED WITH THE PIN YOU MOCK

def auto_water():
    # soil need to be above 88% to not be watered
    # relay led and relay GPIO setup

    soil_moisture = round(random.uniform(0, 90), 2)
    relay = OutputDevice(24, False, False)
    relay_led = LED(21)
    return_msg = ""

    # turn on light and then blink light to show its watering

    if soil_moisture >= 80:
        return_msg = "The plants don't need to be watered"
    else:
        print("turning on relay")
        while soil_moisture <= 80:
            relay_led.on()
            time.sleep(0.5)
            relay_led.blink()
            relay.on()
            soil_moisture += 10.0

        return_msg = "turning off relay plants are watered"
        relay_led.off()
        relay.off()

    return return_msg

    #!!! IMPORTANT MOCKFACTORY() MOCKS THE FUNCITONS / ATTRIBUTES ASSOCATED WITH THE PIN YOU MOCK


def check_status():
    relay_pin = OutputDevice(24, False, False)
    relay_led_pin = LED(21)
    soil_moisture_reader_pin = OutputDevice(12, False, False)
    temp_reader_pin = OutputDevice(9, False, False)

    pin_used = [relay_pin, relay_led_pin, soil_moisture_reader_pin, temp_reader_pin]

    for pin in pin_used:
        try:
            print('Cycling through devices')
            pin.on()
            print(pin.value)
            pin.off()
            print(pin.value)
        except Exception as e:
            relay_pin.off()
            relay_led_pin.off()
            soil_moisture_reader_pin.off()
            temp_reader_pin.off()
            print(e)
            return e

    return "All devices are working"


def soil_tracker():
    soil_moisture_reader_pin = OutputDevice(12, False, False)
    soil_moisture_reader_pin.on()
    soil_moisture_reader_pin.off()

    return ""




# turn_on_relay(90)
# auto_water()
# check_status()
