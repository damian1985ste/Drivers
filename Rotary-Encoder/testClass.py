from rotary_encoder import r_encoder
import time

enc=r_encoder()

b=1
cont=0
while True:
	a,b = enc.rot_encod(b)
	cont = cont + a
	print cont
	time.sleep(0.01)
