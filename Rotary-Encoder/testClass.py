from rotary_encoder import r_encoder
import time

enc=r_encoder()
salida = open("output.txt", "w")

b=1
cont=0
while True:
	#time.sleep(0.1)
	a,b = enc.rot_encod(b)
	#salida.write('A='+str(a))
	#salida.write(', B='+str(b)+'\n')
	cont = cont + a
	print(int(cont))
	#time.sleep(0.01)
