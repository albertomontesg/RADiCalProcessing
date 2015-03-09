import numpy as np
from interface import Interface

#Definim variables globals
f0 = 10.525e9
c = 3e8
lamb = c/f0

class Radar(object):
	def __init__(self, interface):
		self.high = 0
		self.lenght = 0
		self.distance = 0
		self.angle_az = 0
		self.angle_cen = 0

		self.historic_speeds = np.array([])
		self.interface = interface

	def setHeigh(self):
		if self.high == 0:
			self.high = int(raw_input("Please, enter heigh: "))

	def setLenght(self):
		if self.lenght == 0:
			self.lenght = int(raw_input("Please, enter lenght: "))

	def setDistance(self):
		if self.distance == 0:
			self.distance = int(raw_input("Please, enter distance: "))

	def update_stats():
		average = np.average(self.historic_speeds)
		min_s = np.min(self.historic_speeds)
		max_s = np.max(self.historic_speeds)
		self.interface.update_stats(aver = average, min = min_s, max = max_s)
		self.interface.update_histogram(self.historic_speeds)

	def processing(self, f, high, lenght, distance):

		#Caluculem angles
		self.angle_az = np.arctan2(self.high, self.lenght)		
		self.angle_cen = np.arctan2(self.distance, self.lenght)

		#Trobem la velocitat radial a partir de la fd i lambda
		vrad = (f*lamb)/2

		#Calculem la velocitat del cotxe
		v = vrad/(np.cos(self.angle_az)*np.cos(self.angle_cen))
		vkm = v * 3.6

		#Imprimim per pantalla les velocitats
		print '%.2f' % v, " m/s"
		print '%.2f' % vkm, " km/h"

		self.historic_speeds = np.append(self.historic_speeds, vkm)

		#self.interface.show_speed(vkm)
		#self.update_stats(self.historic_speeds)

		return vkm
