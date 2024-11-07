from gpiozero import LED
from time import sleep

# Define the GPIO pin where the LED is connected
led = LED(17)
try:
    while True:
        led.on()  # Turn the LED on
        sleep(1)  # Wait for 1 second
        led.off()  # Turn the LED off
        sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    # Turn off the LED on exit
    led.off()