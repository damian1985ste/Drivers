#!/usr/bin/python
import time
import serial

class rfid:
  def __init__(self):
    '''Esta funcion inicializa la conexion serial al rfid'''
    self.RFID = serial.Serial(
      port='/dev/ttyACM0',
      baudrate=9600,
      stopbits=serial.STOPBITS_ONE,
      xonxoff=True,
      bytesize=serial.EIGHTBITS,
      timeout=3
    )
    if self.RFID.isOpen():
      self.RFID.close()
    self.RFID.open()


  def isOpen(self):
    '''Esta funcion verifica si la conexion serial al rfid esta abierta
    y devuelve un valor true si esta abierta'''
    return self.RFID.isOpen()

  def write(self, wordHex):
    '''Esta funcion escribe en el puerto serial del rfid un comando 
    wordHex en hexadecimal'''
    return self.RFID.write(wordHex)
    #se puede evaluar devolver valor si falla la escritura
    
  def read(self,k):
    '''Esta función lee del puerto serial la cantidad k de bites'''
    while slef.RFID.inWaiting()>0:
      return self.RFID.read(k)
      
  def readTag(self):
    '''Esta funcion envia al rfid el comando de lectura de caravanas
    y luego lee 40 bytes de la informacion enviada al puerto serial.
    Procesa la informacion y retorna el numero de caravana'''
    ### b'\x01\x03\x80\x00\x00\x83' COMANDO LECTURA DE CARAVANA
    self.write(b'\x01\x03\x80\x00\x00\x83')
    time.sleep(1)
    carav = self.read(40) #40 es el valor con el probe la lectura y anduvo
    numCarav = 0 # Procesar el valor de la caravana para retornar un valor util para el operador

  def close(self):
    '''Esta funcion cierra la conexion serial'''
    return self.RFID.close()