#!/usr/bin/python
import time
import serial

class rfid:
  def __init__(self):
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
    return self.RFID.isOpen()

  def write(self, wordHex):
    return self.RFID.write(wordHex)
    #se puede evaluar devolver valor si falla la escritura
    
  def read(self,k):
    while slef.RFID.inWaiting()>0:
      return self.RFID.read(k)
      
  def readTag(self):
    ### b'\x01\x03\x80\x00\x00\x83' COMANDO LECTURA DE CARAVANA
    self.write(b'\x01\x03\x80\x00\x00\x83')
    time.sleep(1)
    carav = self.read(40) #40 es el valor con el probe la lectura y anduvo
    numCarav = 0 # Procesar el valor de la caravana para retornar un valor util para el operador

  def close(self):
    return self.RFID.close()

#out2 =[hex(ord(c)) for c in out]
#out3 = "Lectura: "
#for d in out2:
#    out3 = out3 + "/"+ d 
#print(out3)

