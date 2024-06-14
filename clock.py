import RPi.GPIO as GPIO
import numpy as np
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)

p.start(7.5)

try:
    for i in np.arange(3,12, 0.1):
        print("===============")
        print(time.ctime())
        p.ChangeDutyCycle(i)
        time.sleep(1)
except KeyboardInterrupt:
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    p.stop()
    GPIO.cleanup()

