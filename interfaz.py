#!/usr/bin/python
from RotaryEncoder.rotary_encoder import r_encoder
from beeper.beeper import beeper
from RFID.RI_STU_MRD2 import rfid
from display.st7920 import ST7920

class interfazDR:
	def __init__(self):
		self.re = r_encoder()
		self.beep = beeper()
		self.rfid = rfid()
		self.disp = ST7920()
		
	#FUNCIONES ASOCIADAS AL ROTARY ENCODER	
	def RE_btn_state(self):
		return(self.re.btn_state())
	
	def RE_rot_state(self):
		return(self.re.rot_encod()[0])
		
	#FUNCION ASOCIADAS BEEPER
	def BP_beeper(self, t_pit_sec , k_pitidos = 1, t_sil_sec = 0):
		self.beep.beepXk(k_pitidos, t_pit_sec, t_sil_sec)

	#FUNCIONES ASOCIADAS AL LECTOR RFID
	def RF_readTag(self):
		return(self.rfid.readTag())
		
	#FUNCIONES ASOCIADAS A EL DISPLAY
	def DP_clear(self):
		return(self.disp.clear())
		
	def DP_line(self, x1, y1, x2, y2, set=True):
		return(self.disp.line(x1, y1, x2, y2, set))
	
	def DP_fill_rect(self, x1, y1, x2, y2, set=True):
		return(self.disp.fill_rect(x1, y1, x2, y2, set))
		
	def DP_rect(self, x1, y1, x2, y2, set=True):
		return(self.disp.rect(x1, y1, x2, y2, set))
		
	def DP_plot(self, x, y, set):
		return(self.disp.plot(x, y, set))
		
	def DP_put_text(self, s, x, y):
		return(self.disp.put_text(s, x, y))
		
	def DP_put_textG(self, s, x, y):
		return(self.disp.put_textG(s, x, y))
		
	def DP_put_textB(self, s, x, y):
		return(self.disp.put_textB(s, x, y))
		
	def DP_redraw(self, dx1=0, dy1=0, dx2=127, dy2=63):
		return(self.disp.redraw(dx1, dy1, dx2, dy2))