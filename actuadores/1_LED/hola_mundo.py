from gpiozero import LED
from time import sleep

led = LED(13)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
