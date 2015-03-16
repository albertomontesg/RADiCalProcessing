
import serial

class SerialConnection(object):
	def __init__(self):
		self.serial = serial.Serial('/dev/tty.usbmodemfd131', 9600)
		#self.serial.open()

	def get_data(self):
		# get the frequency count
		value = self.serial.readline()
		
		freq = 0
		if value != '':
			freq = int(value)  ## Parse the value given to get the integer as the frequency counter
			if freq != 0:
				print 'frequency counter:', freq
		return freq

	def close(self):
		self.serial.close()