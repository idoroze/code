import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import requests

url = "http://127.0.0.1:5000/set_stat"


def button_callback(channel):
    print('btn pushed')
    requests.post(url, {'data': 2})


GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Setup event on pin 10 rising edge
GPIO.add_event_detect(40, GPIO.RISING, callback=button_callback)
message = input("Press enter to quit\n\n")  # Run until someone presses enter
# GPIO.cleanup()  # Clean up
