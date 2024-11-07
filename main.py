from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0
    sleep(0.25)
    led.value = 0.25
    sleep(0.25)
    led.value = 0.5
    sleep(0.25)
    led.value = 0.75
    sleep(0.25)
    led.value = 1
    sleep(0.25)
    led.value = 0.75
    sleep(0.25)
    led.value = 0.5
    sleep(0.25)
    led.value = 0.25
    sleep(0.25)
    led.value = 0