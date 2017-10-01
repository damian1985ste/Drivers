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
    '''Esta funcion lee del puerto serial la cantidad k de bites'''
    while self.RFID.inWaiting()>0:
      return self.RFID.read(k)
      
  def readTag(self):
    '''Esta funcion envia al rfid el comando de lectura de caravanas
    y luego lee 40 bytes de la informacion enviada al puerto serial.
    Procesa la informacion y retorna el numero de caravana'''
    ### b'\x01\x03\x80\x00\x00\x83' COMANDO LECTURA DE CARAVANA
    self.write(b'\x01\x03\x80\x00\x00\x83')
    time.sleep(1)
    read = self.read(40) #40 es el valor con el probe la lectura y anduvo
    out2 =[bin(ord(c)) for c in read]
    #print out2
    if len(out2)>13:
      concat = int(out2[9][4:10].zfill(6)+out2[10][2:10].zfill(8)+out2[11][2:10].zfill(8)+out2[12][2:10].zfill(8)+out2[13][2:10].zfill(8),2)
      #print concat
      pais = int(out2[8][2:10].zfill(8)+out2[9][2:4].zfill(2),2)
      #print pais
      #carav = "Lectura: "
      #for d in out2:
      #  carav = carav + "/"+ d 
      return(pais,concat)
    else:
      return 0

  def close(self):
    '''Esta funcion cierra la conexion serial'''
    return self.RFID.close()