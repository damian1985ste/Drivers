from RPi import GPIO
from time import sleep

beep = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(beep, GPIO.OUT)

while True:
  GPIO.output(beep,1)
  sleep(0.1)
  GPIO.output(beep,0)
  sleep(0.5)