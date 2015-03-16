import numpy as np

#Definim variables globals
f0 = 9.6e9
c = 3e8
lamb = c/f0

class Radar(object):
	def __init__(self):
		self.high = 0
		self.length = 0
		self.distance = 0
		self.angle_az = 0
		self.angle_cen = 0

	def setHeight(self):
		if self.high == 0:
			self.high = int(raw_input("Please, enter heigh: "))

	def setLength(self):
		if self.length == 0:
			self.length = int(raw_input("Please, enter length: "))

	def setDistance(self):
		if self.distance == 0:
			self.distance = int(raw_input("Please, enter distance: "))

	def processing(self, f):

		#Caluculem angles
		self.angle_az = np.arctan2(self.high, self.length)		
		self.angle_cen = np.arctan2(self.distance, self.length)

		#Trobem la velocitat radial a partir de la fd i lambda
		vrad = (f*lamb)/2.0

		#Calculem la velocitat del cotxe
		v = vrad/(np.cos(self.angle_az)*np.cos(self.angle_cen))
		vkm = v * 3.6

		#Imprimim per pantalla les velocitats
		if v!= 0:
			print '%.2f' % v, " m/s"
			print '%.2f' % vkm, " km/h"

		#self.interface.show_speed(vkm)
		#self.update_stats(self.historic_speeds)

		return float(vkm)
