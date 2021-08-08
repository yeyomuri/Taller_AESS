import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#Asignacion al pin 17 como pin de salida y PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 30) # Pin 17 a 50 Hz
servo.start(0)

try:
    while True:
        angle = float(input('Ingrese un angulo entre 0° y 180°: '))
        servo.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
finally:
    servo.stop()
    GPIO.cleanup()


