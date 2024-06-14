import RPi.GPIO as GPIO
import time
from enum import Enum

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(7.5)

class State(Enum):
    WATER = 1
    STOP = 2

state = State.STOP

val = {
        State.STOP: 7.5,
        State.WATER: 2.5,
        }
try:
    while True:
        print("===============")
        print(time.ctime())
        print(state.name)

        p.ChangeDutyCycle(val[state])
        time.sleep(3)
        state = State.STOP if state == State.WATER else State.WATER
except KeyboardInterrupt:
    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    p.stop()
    GPIO.cleanup()

