from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED, OutputDevice
from gpiozero.pins.mock import MockPin
import os
import time

# if os.getenv('ENVIRONMENT') == "DEV":

# Device.pin_factory = MockFactory()
Device.pin_factory = MockPin
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
    # relay led and relay GPIO setup
    # relay = OutputDevice(pin=24, active_high=False, initial_value=False)
    mock_relay = MockPin(number=21)    # relay_led = LED(21)
    # mock_led = Device.pin_factory.pin(21)

    #!!! IMPORTANT MOCKFACTORY() MOCKS THE FUNCITONS / ATTRIBUTES ASSOCATED WITH THE PIN YOU MOCK
    # relay_led.

    # if  mock_relay._get_state():
    #     print(mock_relay._get_state())
    #     print(mock_relay.input_with_pull('down'))
    #     print(mock_relay.read())

        # mock_relay.drive_low()
        # print(mock_relay.value)


    # mock_relay.blink()
    # print(mock_relay.drive_low())
    #
    # print(mock_relay)
    # mock_relay.on()

    # while not soil_moisture >= 50:
    # #
    #     if  mock_relay._get_state():
    #         print('turning on relay')
    #         mock_relay.on()
    #         # mock_led.blink()
    #         # time.sleep(10)
    #         # mock_relay.toggle()
    #         # print('turning off relay')
    #         # mock_led.on()
    #         # mock_led.off()
    #     soil_moisture += 10.0

# print("plants are watered")

turn_on_relay(20)