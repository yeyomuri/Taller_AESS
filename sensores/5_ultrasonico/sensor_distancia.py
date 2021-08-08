from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
while True:
    print('Distance: ')
    print((sensor.distance * 100, ))
    sleep(1)