import RPi.GPIO as gpio
import time

def forward(dt):
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(dt)
    gpio.cleanup()

def stop():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.cleanup()

def check():
    gpio.setmode(gpio.BCM)
    gpio.setup(24,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.output(24, False)
    time.sleep(1)       # On la prend toute les 1 seconde
    gpio.output(24, True)
    time.sleep(0.00001)
    gpio.output(24, False)
    while gpio.input(23)==0:  ## Emission de l'ultrason
        debutImpulsion = time.time()

    while gpio.input(23)==1:   ## Retour de l'Echo
        finImpulsion = time.time()

    d = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
    print(d)
    gpio.cleanup()
    return d

d = 10
t = 0
while t<20:
    while d<10:
        d=check()
        t+=1
        print(d)
    forward(0.5)
    stop()
    d=check()
    t+=1
gpio.cleanup()