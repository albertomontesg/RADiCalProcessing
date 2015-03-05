import numpy as np

#Definim variables globals
f0 = 10.525e9
c = 3e8
lamb = c/f0

high = 0
lenght = 0
distance = 0
angle_az = 0
angle_cen = 0

def setHeigh():

	global high

	if high == 0:
		high = int(raw_input("Please, enter heigh: "))

	return high

def setLenght():

	global lenght 

	if lenght == 0:
		lenght = int(raw_input("Please, enter lenght: "))

	return lenght

def setDistance():

	global distance

	if distance == 0:
		distance = int(raw_input("Please, enter distance: "))

	return distance

def computAngles():

	global angle_az
	global angle_cen

	#Caluclem angles
	angle_az = np.arctan2(high, lenght)		
	angle_cen = np.arctan2(distance, lenght)


def processing(f, high, lenght, distance):

	global angle_az
	global angle_cen

	#Trobem la velocitat radial a partir de la fd i lambda
	vrad = (f*lamb)/2

	#Calculem la velocitat del cotxe
	v = vrad/(np.cos(angle_az)*np.cos(angle_cen))
	vkm = v * 3.6

	#Imprimim per pantalla les velocitats
	print '%.2f' % v, " m/s"
	print '%.2f' % vkm, " km/h"

	return v


if __name__ == "__main__":

	high = setHeigh()
	lenght = setLenght()
	distance = setDistance()
	computAngles()

	v = processing(5500, high, lenght, distance)
