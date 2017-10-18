from RPi import GPIO
from time import sleep

en1 = 12
en2 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(en1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(en2, GPIO.IN, GPIO.PUD_UP)

counter = 0
en1LastState = GPIO.input(en1)

try:

        while True:
                en1State = GPIO.input(en1)
                #print("entrada 1: "+str(en1State))
                #sleep(0.2)
                en2State = GPIO.input(en2)
                #print("entrada 2: "+str(en2State))
                #sleep(0.2)
                if en1State != en1LastState:
                        if en2State != en1State:
                                counter += 1
                        else:
                                counter -= 1
                        print counter
                en1LastState = en1State
                sleep(0.01)
finally:
        GPIO.cleanup()
