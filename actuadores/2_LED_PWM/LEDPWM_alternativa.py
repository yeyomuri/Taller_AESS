import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

ledPWM = GPIO.PWM(13, 100)
ledPWM.start(50)

while True:
    brightness_s = float(input("Ingrese un valor entre 0 y 100: "))
    ledPWM.ChangeDutyCycle(brightness_s)
    