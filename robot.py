import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

def forward(dt):
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(dt)

def back(dt):
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(dt)


forward(2)
back(2)

gpio.cleanup()