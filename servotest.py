import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)

p.start(7.5)

state = True
labels = {
        True: "water",
        False: "stop",
        }

val = {
        True: 7.5,
        False: 2.5,
        }
try:
    while True:
        print("===============")
        print(time.ctime())
        print(labels[state])
        state = not state

        p.ChangeDutyCycle(val[state])
        time.sleep(.3)
except KeyboardInterrupt:
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    p.stop()
    GPIO.cleanup()

