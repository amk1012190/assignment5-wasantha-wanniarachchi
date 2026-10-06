from machine import Pin, PWM
from time import sleep

e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

SPEED = 32767
TURN_90_TIME = 0.8
FORWARD_HALF_METER = 2

def stop():
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(0.5)

def move_forward():
    m1.value(1)
    m2.value(2)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(FORWARD_HALF_METER)
    stop()

def reverse():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(FORWARD_HALF_METER)
    stop()

def turn_left():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(TURN_90_TIME)
    stop()

def turn_right():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(TURN_90_TIME)
    stop()

def turn_around():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(SPEED)
    e2.duty_u16(SPEED)
    sleep(TURN_90_TIME * 2)
    stop()

sleep(2)

move_forward()
turn_right()
move_forward()
turn_right()
move_forward()
turn_left()
move_forward()
turn_left()
move_forward()
turn_around()
reverse()
