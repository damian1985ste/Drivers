#!/usr/bin/python
from RPi import GPIO
import time

class beeper:
  def __init__(self):
    '''Esta funcion inicializa la GPIO PIN 21 para el beeper'''
    self.pin = 21
    self.gpio = GPIO
    self.gpio.setmode(GPIO.BCM)
    self.gpio.setwarnings(False)
    self.gpio.setup(self.pin, GPIO.OUT)

  def beep(self, t_sec):
    ''' Esta funcion emite un pitido de duracion t_sec'''
    self.gpio.output(self.pin,1)
    time.sleep(t_sec)
    self.gpio.output(self.pin,0)
    
  def beepXk(self, k_pitidos, t_pit_sec = 0.2, t_sil_sec = 0.2):
    '''Esta funcion emite un numero k_pitidos de pitidos
    sonando por un tiempo en segundos de t_pit_sec y haciendo
    un silencio de t_sil_sec segundos para cada pitido'''
    for k in range(k_pitidos):
      self.gpio.output(self.pin,1)
      time.sleep(t_pit_sec)
      self.gpio.output(self.pin,0)
      time.sleep(t_sil_sec)