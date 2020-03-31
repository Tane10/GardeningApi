from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button, LED, output_devices
import os
import piFunctions as pifunc


def check_module_status():
    '''
    Check all connections are working and return back report in message.
    This will be called daily at an set time during the day as a standard
    report helping with maintenance.
    os.getenv('ENVIRONMENT')


    # Set the default pin factory to a mock factory

    # Construct a couple of devices attached to mock pins 16 and 17, and link the
    # devices
    led = LED(17)
    btn = Button(16)
    led.source = btn

    # Here the button isn't "pushed" so the LED's value should be False
    print(led.value)

    # Get a reference to mock pin 16 (used by the button)
    btn_pin = Device.pin_factory.pin(16)

    # Drive the pin low (this is what would happen electrically when the button is
    # pushed)
    btn_pin.drive_low()
    sleep(0.1) # give source some time to re-read the button state
    print(led.value)

    btn_pin.drive_high()
    sleep(0.1)
    print(led.value)

    '''

    if os.getenv('ENVIRONMENT') == "DEV":
        Device.pin_factory = MockFactory()

    led = LED(17)
    print(led.value)

    checking_device_msg = "Everything is connected and working"
    return checking_device_msg


def water_plants():
    '''
    Check soil moisture. if needed to be watered then allow to be watered,
    if soil is at perfect level then allow user to over write and water plants
    but give warning.
    Runs auto every day
    '''
    return pifunc.auto_water()


def soil_tracker():
    '''
    water tracker send a time stamped with soil and light readings to mongoDB
    this is for easy tracking / if needed to stats then its implemented
    '''

    soil_moisture = "50.5%"
    light_val = "102"
    soil_info = "Here is your soil and light info: " + soil_moisture + " light value: " + light_val
    return soil_info


def temp_humidity_check():
    '''
    check the temp and humidity and sends me an update with temp and humidty
     of the plants / environment
    '''

    temp = "18.0 c"
    humidity = "20%"
    temp_humidity_info = "Temperature is " + temp + "humidity is " + humidity
    return temp_humidity_info


def picture_plants():
    '''
    just takes a picture of the plants and send to me.
    can se set up auto 1 week intivals and added to gridfs to track progress
    '''

    pic_msg = "sending you some plant pics"
    return pic_msg


def shutdown(pin):
    '''
    kills the process but will be warned/ could be used the restart things

    '''

    shutdown_msg = "Are you sure you want to shutdown"
    return shutdown_msg

water_plants()

print("can we sync it")

