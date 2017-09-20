from RPi import GPIO
import time


class r_encoder:
  def __init__(self):
    '''Esta funcion inicializa las GPIO 12 y 16 para el rotary
    encoder y el GPIO 20 para el boton del encoder'''
    self.en1 = 12
    self.en2 = 16
    self.btn = 20 
    self.gpio = GPIO
    self.gpio.setmode(GPIO.BCM)
    self.gpio.setup(self.en1, GPIO.IN, GPIO.PUD_UP)
    self.gpio.setup(self.en2, GPIO.IN, GPIO.PUD_UP)
    self.gpio.setup(self.btn, GPIO.IN, GPIO.PUD_UP)
    
  def btn_state(self):
    '''Esta funcion devuelve el estado instantaneo del boton'''
    if self.gpio.input(self.btn):
      return(False)
    else: 
      return(True)
  
  def btn_t_pres(self):
    '''Esta funcion devuelve el tiempo que el boton esta presionado. 
    retorna t_seg que es el tiempo en segundos si el boton esta presionado
    y -1 si el boton no esta presionado. '''
    if self.btn_state():
      #contar tiempo presionado
      k=0
      while self.btn_state():
        time.sleep(0.01)
        k=k+1
      return k*0.01
    else:
      #no esta presionado -1
      return -1
      
  def btn_stat_pres(self,x_sec):
    '''Esta fucion devuelve si el boton fue presionado solamente, si se 
    mantuvo apretado x_sec segundos o si no esta prsionado. Retorna 2 en
    caso que el boton se mantenga presionado, 1 si solo se presiono y -1
    si no fue apretado'''
    if self.btn_state():
      rep = x_sec/0.01
      k=0
      while self.btn_state() and k<rep:
        time.sleep(0.01)
        k+=1
      if k==rep:
        return 2
      else:
        return 1
    else:
      return -1
      
  def rot_encod(self, en1LastState = 1):
    '''Esta funcion devuelve el movimiento del encoder. 0.5 si se movio hacia 
    un lado y -0.5 si se movio al otro lado'''
    en1State = self.gpio.input(self.en1)
    en2State = self.gpio.input(self.en2)
    if en1State != en1LastState:
      if en2State != en1State:
        return(-1,en1State)
      else:
        return(1,en1State)
    else:
      return(0,en1LastState)
      
          
  def cle_rot_enc_GPIO(self):
    '''Esta funcion lipia las configuraciones de los pines de la placa'''
    self.gpio.cleanup()
