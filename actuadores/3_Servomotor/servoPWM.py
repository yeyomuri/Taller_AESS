import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
servo1 = GPIO.PWM(17, 50)

servo1.start(0)
time.sleep(2)

duty = 2 # 0°

while duty <= 12: # 180°
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    
time.sleep(2)
servo1.ChangeDutyCycle(7) #90°
time.sleep(2)
servo1.ChangeDutyCycle(2) #0°
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

#Limpia  y finaliza

servo1.stop()
GPIO.cleanup()


