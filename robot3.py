import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.setup(24,gpio.OUT)
gpio.setup(23,gpio.IN)

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

def right():
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(0.5)

def left():
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(0.5)

def stop():
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, False)

def check():
    gpio.output(Trig, False)
    time.sleep(1)       # On la prend toute les 1 seconde
    gpio.output(24, True)
    time.sleep(0.00001)
    gpio.output(24, False)
    while gpio.input(23)==0:  ## Emission de l'ultrason
        debutImpulsion = time.time()

    while gpio.input(23)==1:   ## Retour de l'Echo
        finImpulsion = time.time()

    d = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
    return d

d = 10
while t<20:
    while d<10:
        d=check()
    foward(0.5)
    stop()
    d=check()

gpio.cleanup()